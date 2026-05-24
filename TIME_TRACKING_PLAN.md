# Fund Team Time Tracking & Sweat-Equity Reimbursement Plan

**Audience:** Founding partners and anyone joining the management company (ManCo) before or after first close.
**Purpose:** Capture true (not self-reported) time spent during the pre-capital phase so it can be repaid from the ManCo budget over the first 24 months after first close, with documentation that holds up to LP, auditor, and IRS scrutiny.

---

## 1. The short version

- **Track time automatically.** Every partner installs a passive desktop tracker that records app/window/file activity in the background. No manual timers. No screenshots. No keystroke logging.
- **Primary tool: Memtime** (cross-platform, raw activity stays local on each laptop) — or **Timing** if the whole team is on Mac.
- **Free corroborating layer: ActivityWatch** on every machine as an independent, open-source audit trail.
- **Each partner signs a one-page consent + deferred compensation agreement *before* installing anything.** Backdating is the #1 audit red flag.
- **Weekly:** 10 minutes to tag the previous week's auto-captured blocks into projects (Fundraising / Diligence / Formation / Ops / LP Comms).
- **Monthly:** Partner-signed summary of hours by category goes into a shared ledger.
- **Repayment:** Treated as **deferred guaranteed payments from the ManCo** (not a fund expense), paid out evenly over the first 24 months post-close at a pre-agreed hourly rate or monthly cap.

---

## 2. Why this structure (the non-obvious parts)

Three things drove the design — read these before substituting your own preferences.

1. **Founder time is almost never a *fund* expense.** Industry standard is that pre-fund founder hours are not reimbursed by LP capital — they're either compensated via carry/management-fee draw post-close, or they're paid out of the **ManCo's own budget** (the 2% management-fee revenue stream) as deferred founder compensation. Co-mingling founder time into "organizational expenses" of the fund itself is an LPA violation risk and a classic LP red flag. We're routing everything through the ManCo deliberately.

2. **The legal posture for partners ≠ employees.** LLC/LP partners are self-employed under IRS rules and are *not* covered by state employee-monitoring notice statutes (NY 52-c, CT 31-48d, DE 705). But the moment we hire a W-2 employee or a 1099 contractor, those statutes kick in for that person's state. So we're writing the consent doc to satisfy NY's statutory language from day one — it's defensible everywhere and we won't have to redo it.

3. **Tooling category matters for optics.** Hubstaff, Time Doctor, and Insightful screenshot and keylog by default. They're built for employers to surveil contractors. Using them on yourself signals mistrust to anyone who later reviews this arrangement — LPs, partners' spouses in a divorce, an IRS auditor, a journalist. We picked tools built for *principals tracking themselves*.

---

## 3. The tool stack

### Primary tracker — pick ONE based on team OS mix

#### Option A: **Memtime** (recommended if any partner is on Windows or Linux)
- Captures every program, file, browser tab, email, and calendar entry minute-by-minute as a color-coded daily timeline.
- **Raw activity data never leaves the laptop.** Only the time entries you explicitly assign to a project sync to their cloud. This is the killer feature.
- No screenshots, no keystrokes, no webcam.
- macOS, Windows, Linux.
- ~$18/user/month annual (Connect tier — needed for QuickBooks/Xero sync).
- 14-day trial, no credit card.
- https://www.memtime.com

#### Option B: **Timing** (recommended if all-Mac team)
- Same auto-capture model, plus URL/document/Zoom call tracking and iPhone Screen Time import.
- Rule-based auto-routing ("files in `~/FundCo/` → project: Fund Ops").
- AppleScript + REST API for clean monthly export.
- macOS only.
- $16/user/month annual (Connect tier).
- https://timingapp.com

### Free corroborating layer — install on EVERY machine

**ActivityWatch** (https://activitywatch.net) — open source, MPL-2.0, fully local, no cloud. Captures app/window/browser activity independently. This is our hedge: if the primary tracker has a bug, gets discontinued, or someone disputes a month two years from now, we have an independent record stored locally and exportable to git.

### Optional: WakaTime for any partner who codes
Free, IDE-only, never captures source content. Layer it on for richer detail; don't make it the system of record.

### Hard "no"s
**Hubstaff, Time Doctor, Insightful, ActivTrak, Teramind, Veriato, DeskTime.** Surveillance-class tools. Don't install them on partners.

---

## 4. Reimbursement structure

### Rate — pick one approach, write it down before any work is tracked

**Approach 1 — Hourly imputed rate (cleaner audit trail).**
$100–$175/hour per partner. Stay at or below the salary the partner will actually draw from the ManCo post-close — rate inflation is the #1 LP red flag. For a Fund I principal benchmarking to a $150–$250K annual draw, $120–$150/hour is the defensible band.

**Approach 2 — Monthly stipend with cap (simpler).**
$10K–$15K/month per partner, deferred, total capped at a fixed dollar amount per partner. Pay out over 24 months post-close.

Either approach: the dollar value of pre-close hours times rate = a deferred-comp liability on the ManCo's books, paid in 24 equal monthly installments starting at first close.

### Tax classification
Reimbursement to partners of an LLC/LP ManCo should be structured as **guaranteed payments** (IRS Pub 541) — deductible by the ManCo, ordinary income + self-employment tax to the recipient. **Do not** 1099 partners of their own partnership (IRS disallows it). **Do not** classify as a partnership distribution unless your CPA specifically directs that route. Confirm with tax counsel before first close.

### Documentation set (what the auditor expects)
1. **Pre-signed deferred compensation agreement** specifying rate, total cap per partner, and 24-month payout schedule. Signed *before* tracking starts. Backdating is fatal.
2. **ManCo board / managing member resolution** approving the deferred comp arrangement.
3. **Contemporaneous time logs** (the Memtime/Timing export) — entries made within ~1 week of the work, not reconstructed.
4. **Monthly hours summary** by partner and category, signed by all partners (mutual attestation).
5. **PPM / LPA disclosure** that the ManCo carries deferred founder compensation obligations — coordinate with fund counsel.

---

## 5. Consent & privacy one-pager (template — every participant signs before installing)

> **Time-Accounting Consent — [ManCo LLC]**
>
> 1. **Purpose.** Time captured by this software is used solely for (a) calculating deferred founder compensation owed under the [DATE] Deferred Compensation Agreement, (b) ManCo tax substantiation, and (c) each participant's own time accounting. It is not used for performance evaluation or surveillance.
> 2. **What is captured.** Application name, active window title, file/document name, idle vs. active status, and the project tag the participant assigns to each block.
> 3. **What is NOT captured.** Keystrokes, passwords, screenshots, webcam, microphone, browser page content, personal-device data outside the participant's declared working-hours window.
> 4. **Devices in scope.** The participant's primary work laptop only. Working-hours window: [e.g., 7am–8pm local].
> 5. **Pause / personal time.** The participant may pause the tracker at any time for personal matters with no obligation to justify the gap.
> 6. **Access.** Each participant sees their own raw data. Monthly aggregated summaries (hours by category) are shared symmetrically among all participants — no one-way dashboards.
> 7. **Retention.** Raw logs: 90 days. Aggregated monthly summaries and project allocations: 7 years (tax/reimbursement records).
> 8. **Rights.** Each participant may review, correct, export, or delete their own data and may revoke consent on 14 days' written notice. Revocation does not retroactively invalidate already-logged time.
> 9. **Acknowledgment.** Participant acknowledges that any and all activity tracked by the software described above may be subject to monitoring at any and all times and by any lawful means consistent with this agreement.
>
> Signed: _____________________  Date: __________
> (NY statutory language is included in section 9 verbatim so this document satisfies notice requirements in every state we expect to operate in.)

**If anyone on the team is in the EU/UK:** consent is *not* a valid legal basis under GDPR for workplace monitoring (power imbalance). Switch to a Legitimate Interest Assessment + DPIA before installing. Get counsel.

---

## 6. The weekly + monthly cadence

### Daily — zero overhead
Tracker runs in the background. Nothing to do.

### Weekly — 10 minutes, ideally Friday afternoon
1. Open Memtime/Timing. Look at the week's timeline.
2. Drag-assign unassigned blocks to one of these project tags:
   - **Fundraising** (LP outreach, deck work, pitching)
   - **Diligence** (researching specific opportunities)
   - **Formation & Legal** (entity setup, docs, counsel calls)
   - **Ops & Admin** (banking, software setup, bookkeeping)
   - **LP / Investor Comms** (existing relationship maintenance)
   - **Personal / Non-fund** (anything not reimbursable — be honest)
3. Export the week's CSV to the shared `/time-tracking/[partner-name]/` folder.

### Monthly — 30 minutes, first business day of the month
1. Each partner generates a one-page summary: hours by category for the prior month.
2. Drop into the shared ledger (Google Sheet or Notion — doesn't matter; pick one).
3. All partners sign (DocuSign or e-sig) the monthly summary as mutual attestation.
4. Update the running deferred-comp liability total per partner.

### Quarterly — 15 minutes
Reconcile against the ManCo books. Make sure the deferred-comp liability the bookkeeper has matches the ledger.

---

## 7. Rollout — week by week

**Week 0 (this week)**
- [ ] [Founder] reads this plan, edits to taste, decides hourly-rate vs. monthly-stipend approach.
- [ ] [Founder] sends the Deferred Compensation Agreement template to fund counsel for review. Mention this is **ManCo-level deferred comp, not a fund expense**, so the LPA doesn't need to address it (but the PPM should disclose the ManCo carries the obligation).
- [ ] [Founder] picks Memtime vs. Timing based on team OS mix.

**Week 1 — Founder-only pilot**
- [ ] [Founder] installs the primary tracker + ActivityWatch on his own machine first. Tracks for a full week. Shares the raw weekly export with both partners — no editing, warts and all. This sets the trust tone.

**Week 2 — Partner onboarding**
- [ ] [Founder] schedules a 45-min walkthrough call.
- [ ] All three sign the Consent & Deferred Comp Agreement (pre-dated as of the signing day, not the start of work).
- [ ] Partners install primary tracker + ActivityWatch.
- [ ] Set up the shared `/time-tracking/` folder structure in Google Drive / Dropbox.

**Week 3 — Process trial**
- [ ] First weekly tagging session, end of week. All three partners do it on the same Friday and share notes on friction.
- [ ] Refine project categories if needed.

**Week 4 — First monthly close**
- [ ] First monthly summary signed by all partners.
- [ ] First deferred-comp liability entry made on the ManCo books.

**Ongoing — every new hire**
- [ ] Before W-2 or 1099 work starts: signed consent doc, NY statutory notice language, install trackers. If the new hire is in NY, CT, DE, or CO, double-check the state-specific language with counsel.

---

## 8. The kickoff message to the team

Copy/paste, edit, send:

> Team —
>
> One housekeeping item before we go any further. The three of us are putting in real hours pre-close and I want all of us paid back fairly once we have a budget. That means we need a clean, contemporaneous record of time spent — the kind that holds up to an auditor and to ourselves two years from now when memories have faded.
>
> Self-reported timesheets don't survive contact with reality. So we're going to use a passive tracker (Memtime / Timing — TBD on which) that runs in the background and records what we're working on automatically. Importantly: **no screenshots, no keystroke logging, no surveillance creep**. Raw activity data stays on each of our laptops. Only the project tags we assign each week sync to the shared ledger.
>
> Repayment will be structured as deferred founder compensation from the ManCo, paid out over the first 24 months after first close, at $[RATE]/hour or $[X]K/month — whichever we agree on in the next 48 hours. This is a ManCo obligation, not a fund expense.
>
> I'm installing on my machine this week and will share my raw weekly export with both of you on Friday so you can see exactly what gets captured before signing anything. Consent doc + deferred comp agreement to follow once you've seen the data.
>
> Questions / objections welcome — better to hash them out now than in month nine.

---

## 9. Open decisions (Founder must answer before Week 0 closes)

1. **OS mix on the team?** Picks Memtime vs. Timing.
2. **Hourly rate vs. monthly stipend?** And the specific number.
3. **Hard cap per partner** (total deferred comp dollars, not just hours).
4. **State of residence for each partner?** If any is NY, CT, DE, CO, CA, or in the EU/UK — flag to counsel.
5. **What's the bookkeeper / fund admin?** They need to be looped in to carry the deferred-comp liability properly.
6. **Counsel for the deferred-comp agreement** — fund counsel or separate?

---

## 10. Sources behind the recommendations

Tools — [Memtime](https://www.memtime.com), [Timing](https://timingapp.com), [ActivityWatch](https://activitywatch.net), [RescueTime](https://www.rescuetime.com), [WakaTime](https://wakatime.com).

Fund structure — [Withum on guaranteed payments vs. distributions](https://www.withum.com/resources/management-company-series-how-to-pay-partners-guaranteed-payments-vs-distributions/), [IRS Pub 541](https://www.irs.gov/publications/p541), [Foresight on ManCo budgeting](https://foresight.is/docs/management-company/), [Decile Group on fund expense caps](https://decilegroup.com/posts/how-do-fund-expenses-work-with-the-fund-expense-cap-as-set-in-the-lpa), [VC Lab on emerging managers](https://govclab.com/2026/03/25/emerging-manager-venture-capital-the-complete-guide-for-2026/).

Privacy / legal — [NY Civil Rights Law 52-c](https://law.justia.com/codes/new-york/cvr/article-5/52-c-2/), [Mosey state-by-state monitoring guide](https://mosey.com/blog/notice-of-electronic-monitoring-compliance-guide/), [California CCPA employee data](https://www.employee-monitoring.net/compliance/california-employee-monitoring-laws), [GDPR employee monitoring](https://www.worktime.com/blog/employee-monitoring/gdpr-employee-monitoring).
