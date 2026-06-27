"""
LLM abstraction.

Two modes, chosen automatically:
  * If ANTHROPIC_API_KEY is set  -> real Claude calls (claude-opus-4-8 / sonnet).
  * Otherwise                    -> a deterministic local engine so the demo
                                    ALWAYS runs offline with zero dependencies.

Every AI module in this demo routes its "intelligence" through here, and prints
which engine produced the result, so a viewer can see exactly where the model
sits and what is heuristic fallback.
"""
import json
import os
import ssl
import urllib.request

API_KEY = os.environ.get("ANTHROPIC_API_KEY")
USE_LLM = bool(API_KEY)
MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-8")
ENGINE = "Claude (" + MODEL + ")" if USE_LLM else "local heuristic engine (offline)"


def _ssl_ctx():
    bundle = "/root/.ccr/ca-bundle.crt"
    if os.path.exists(bundle):
        return ssl.create_default_context(cafile=bundle)
    return ssl.create_default_context()


def complete(system, user, max_tokens=1024):
    """Return raw text from Claude. Raises on any failure (caller falls back)."""
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        method="POST",
        headers={
            "x-api-key": API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        data=json.dumps({
            "model": MODEL,
            "max_tokens": max_tokens,
            "system": system,
            "messages": [{"role": "user", "content": user}],
        }).encode(),
    )
    with urllib.request.urlopen(req, context=_ssl_ctx(), timeout=60) as r:
        body = json.loads(r.read())
    return "".join(b.get("text", "") for b in body.get("content", []))


def complete_json(system, user, max_tokens=1024):
    """Ask Claude for JSON and parse it. Raises on failure."""
    txt = complete(system + "\nReturn ONLY valid JSON, no prose.", user, max_tokens)
    txt = txt.strip()
    if txt.startswith("```"):
        txt = txt.split("```", 2)[1].lstrip("json").strip()
    return json.loads(txt)


def selftest():
    """Ping the model so a viewer can confirm the Claude wiring is live."""
    if not USE_LLM:
        return False, "no ANTHROPIC_API_KEY set -> running offline heuristic engine"
    try:
        txt = complete("You are a healthcheck.", "Reply with the single word: OK", 10)
        return True, f"Claude reachable ({MODEL}) -> {txt.strip()[:20]}"
    except Exception as e:
        return False, f"key set but call failed ({type(e).__name__}: {e}) -> using offline engine"
