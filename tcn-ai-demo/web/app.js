// Faithful client-side port of nlc.py (parse_rule + eligible) so the rule box
// runs live in the browser. Analytics + ledger are loaded precomputed.

const STRICT = new Set(["FL", "NY", "OK"]);
const STATE_PHRASES = {
  "new york":"NY","ny":"NY","florida":"FL","fl":"FL","texas":"TX","tx":"TX",
  "california":"CA","ca":"CA","utah":"UT","ut":"UT","oklahoma":"OK","ok":"OK",
  "illinois":"IL","il":"IL","georgia":"GA","ga":"GA","washington":"WA","wa":"WA",
  "arizona":"AZ","az":"AZ"
};

function parseRule(text){
  const t = text.toLowerCase();
  const preds = [];
  const blocky = ["don't call","dont call","no call","skip","block"].some(k=>t.includes(k));
  const seen = new Set();
  for (const [phrase,code] of Object.entries(STATE_PHRASES)){
    const re = new RegExp("\\b"+phrase.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")+"\\b");
    if (!seen.has(code) && blocky && re.test(t)){ preds.push({type:"block_state",state:code}); seen.add(code); }
  }
  let m = t.match(/(\d+)\s*(?:attempts|calls|times)/);
  if (m) preds.push({type:"max_attempts", n:+m[1]});
  m = t.match(/before\s*(\d+)\s*(am|pm)?/);
  if (m) preds.push({type:"no_call_before", hour:+m[1] + (m[2]==="pm" && +m[1]!==12 ? 12:0)});
  m = t.match(/after\s*(\d+)\s*(am|pm)?/);
  if (m) preds.push({type:"no_call_after", hour:+m[1] + (m[2]==="pm" && +m[1]!==12 ? 12:0)});
  if (t.includes("written consent") || t.includes("unless we have consent")) preds.push({type:"require_written_consent"});
  if (t.includes("do not call") || t.includes("national dnc") || t.includes("dnc list")) preds.push({type:"block_national_dnc"});
  return preds;
}

function eligible(c, preds){
  const r = [];
  const hour = c.local_hour;
  if (c.consent==="revoked" || c.on_internal_dnc) r.push("Internal DNC / consent revoked (TCPA)");
  if (c.is_known_litigator) r.push("Known TCPA litigator (risk policy)");
  if (c.on_national_dnc && c.consent!=="written") r.push("National DNC without written consent (TCPA/TSR)");
  const [low,high] = STRICT.has(c.state) ? [8,20] : [8,21];
  if (hour<low || hour>=high) r.push(`Outside calling hours ${low}:00-${high}:00 local (now ${hour}:00, ${c.state})`);
  if (c.attempts_last_7d>=7) r.push(`Reg F 7-in-7 exceeded (${c.attempts_last_7d} attempts/7d)`);
  if (c.reassigned_risk) r.push("Reassigned-number risk -- verify before dialing");
  for (const p of preds){
    if (p.type==="block_state" && c.state===p.state) r.push(`User rule: blocked state ${p.state}`);
    else if (p.type==="max_attempts" && c.attempts_last_7d>=p.n) r.push(`User rule: max ${p.n} attempts (has ${c.attempts_last_7d})`);
    else if (p.type==="require_written_consent" && c.consent!=="written") r.push("User rule: written consent required");
    else if (p.type==="no_call_before" && hour<p.hour) r.push(`User rule: no calls before ${p.hour}:00 (now ${hour}:00)`);
    else if (p.type==="no_call_after" && hour>=p.hour) r.push(`User rule: no calls after ${p.hour}:00 (now ${hour}:00)`);
    else if (p.type==="block_national_dnc" && c.on_national_dnc) r.push("User rule: skip all National DNC numbers");
  }
  return {allow: r.length===0, reasons: r};
}

let CONTACTS = [];
const $ = s => document.querySelector(s);

function runNLC(){
  const preds = parseRule($("#rule").value);
  $("#parsed").textContent = preds.length ? "parsed → " + JSON.stringify(preds) : "parsed → (no extra rules; baseline federal rules still apply)";
  let allow=0, block=0; const samples=[]; let example=null;
  for (const c of CONTACTS){
    const e = eligible(c, preds);
    if (e.allow){ allow++; if(!example) example=c; }
    else { block++; if (samples.length<8) samples.push([c,e.reasons]); }
  }
  $("#allow").textContent = `ALLOW: ${allow}`;
  $("#block").textContent = `BLOCK: ${block}`;
  const tb = $("#elig tbody"); tb.innerHTML="";
  for (const [c,reasons] of samples){
    tb.insertAdjacentHTML("beforeend",
      `<tr><td>${c.id}</td><td>${c.name}</td><td>${c.state}</td><td>${c.local_hour}:00</td>
      <td>${c.consent}</td><td class="no">BLOCK</td>
      <td class="reasons">${reasons.join("<br>")}</td></tr>`);
  }
  if (example){
    tb.insertAdjacentHTML("beforeend",
      `<tr><td>${example.id}</td><td>${example.name}</td><td>${example.state}</td>
      <td>${example.local_hour}:00</td><td>${example.consent}</td>
      <td class="ok">ALLOW</td><td class="reasons">safe to dial</td></tr>`);
  }
}

function renderAnalytics(d){
  $("#fails").textContent = `${d.fails} of ${d.rows.length} calls auto-flagged FAIL for review.`;
  const tb = $("#analytics tbody"); tb.innerHTML="";
  for (const r of d.rows){
    tb.insertAdjacentHTML("beforeend",
      `<tr><td>${r.id}</td><td>${r.channel}</td><td>${r.sentiment}</td>
      <td>${r.risk}</td><td>${r.qa}</td>
      <td class="grade-${r.grade}">${r.grade}</td>
      <td class="reasons">${r.flags.map(f=>"["+f.severity+"] "+f.label).join("<br>")||"&mdash;"}</td></tr>`);
  }
}

function renderLedger(d){
  const rows = [];
  rows.push(`<div class="lrow"><span class="k">Records (immutable)</span><span>${d.records}</span></div>`);
  for (const r of d.first)
    rows.push(`<div class="lrow"><span class="k">seq ${r.seq} · ${r.type}</span>
      <span class="lhash">${JSON.stringify(r.payload)} · hash ${r.hash}…</span></div>`);
  rows.push(`<div class="lrow"><span class="k">Chain integrity</span><span class="${d.integrity?'good':'bad'}">${d.integrity?'VALID — not tampered':'BROKEN'}</span></div>`);
  rows.push(`<div class="lrow"><span class="k">Revocation honored (10-day rule)</span><span class="${d.revocation.honored?'good':'bad'}">${d.revocation.honored}</span> <span class="lhash">${d.revocation.detail}</span></div>`);
  rows.push(`<div class="lrow"><span class="k">Rogue dial after opt-out</span><span class="bad">${d.violation.detected?'VIOLATION DETECTED':'—'}</span> <span class="lhash">${d.violation.detail}</span></div>`);
  rows.push(`<div class="lrow"><span class="k">After-the-fact edit of a record</span><span class="bad">${d.tamper.detected?'TAMPER DETECTED at seq '+d.tamper.bad_seq:'—'}</span></div>`);
  $("#ledger").innerHTML = rows.join("");
}

Promise.all([
  fetch("contacts.json").then(r=>r.json()),
  fetch("analytics.json").then(r=>r.json()),
  fetch("ledger.json").then(r=>r.json()),
]).then(([c,a,l])=>{
  CONTACTS=c; runNLC(); renderAnalytics(a); renderLedger(l);
  $("#rule").addEventListener("input", runNLC);
  document.querySelectorAll("button.ex").forEach(b=>
    b.addEventListener("click",()=>{ $("#rule").value=b.textContent; runNLC(); }));
});
