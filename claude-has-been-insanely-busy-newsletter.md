# Claude Has Been INSANELY Busy

**An AI Boss Newsletter — March 20, 2026**

---

Claude has been insanely busy.

I feel like there's a new release every day — sometimes multiple a day. If you blinked this month, you missed 5 announcements.

Here's everything Anthropic shipped in the last 10 business days. Buckle up.

---

## The Releases (March 6–20, 2026)

### March 18 — Model Capability API Fields
Anthropic added `max_input_tokens`, `max_tokens`, and a `capabilities` object to the Models API. You can now query the API to discover exactly what each model supports — no more guessing.

[API Release Notes](https://platform.claude.com/docs/en/release-notes/overview)

---

### March 18 — Largest AI User Study Ever Published
Anthropic published results from a study where they invited Claude.ai users to share how they use AI. Nearly **81,000 people** participated — the largest and most multilingual qualitative study of its kind.

[Anthropic News](https://www.anthropic.com/news)

---

### March 17 — Claude Code v2.1.76+ Bug Fixes & Performance
- Fixed washed-out Claude orange color in VS Code/Cursor terminals
- Added `ANTHROPIC_CUSTOM_MODEL_OPTION` env var for the `/model` picker
- Fixed `ANTHROPIC_BETAS` being silently ignored with Haiku models
- Improved memory usage and startup time when resuming large sessions

[Claude Code Changelog](https://code.claude.com/docs/en/changelog)

---

### March 16 — Extended Thinking Display Control
New `display` field for extended thinking lets you **omit thinking content** from responses for faster streaming. Set `thinking.display: "omitted"` — billing unchanged, signatures preserved for multi-turn continuity.

[API Release Notes](https://platform.claude.com/docs/en/release-notes/overview)

---

### March 15 — Double Usage Limits Promotion Begins
Anthropic **doubled usage limits** for Free, Pro, Max, and Team plans during off-peak hours (weekends + weekdays 8AM–2PM ET). Runs through March 27. Free users get access to Claude's most capable model — not a stripped-down version.

[WebProNews Coverage](https://www.webpronews.com/anthropics-march-2026-claude-promotion-what-you-need-to-know-about-the-free-usage-boost/) | [Android Headlines](https://www.androidheadlines.com/2026/03/claude-double-usage-limits-march-2026-promotion.html)

---

### March 14 — Claude Code: MCP Elicitation & More
Massive Claude Code update:
- **MCP Elicitation Support** — MCP servers can now request structured input mid-task via interactive dialog
- New Elicitation and ElicitationResult hooks
- `-n / --name` CLI flag for startup
- `worktree.sparsePaths` for large monorepos
- PostCompact hook
- `/effort` command (set model effort level)
- Configurable session quality survey

[Claude Code Releases](https://github.com/anthropics/claude-code/releases)

---

### March 13 — 1M Token Context Window Goes GA
The **1 million token context window** is now generally available for Claude Opus 4.6 and Sonnet 4.6 at **standard pricing**. No beta header required. Dedicated 1M rate limits removed. Media limit raised from 100 to **600 images or PDF pages** per request.

[API Release Notes](https://platform.claude.com/docs/en/release-notes/overview)

---

### March 13 — Claude Code: Opus 4.6 Gets 1M Context + UI Updates
- Opus 4.6 boosted to 1M context on all plans
- `/color` command added
- Session name on the prompt bar
- Memory freshness timestamps
- Hook sources now visible
- Voice mode fixes
- macOS speedup

[Claude Code Changelog](https://code.claude.com/docs/en/changelog)

---

### March 12 — Inline Visualizations
Claude can now create **custom charts, diagrams, and visualizations inline** in its responses. No more switching to external apps.

[Anthropic News](https://www.anthropic.com/news)

---

### March 12 — Claude Code: Actionable Context Suggestions
Claude Code now identifies context-heavy tools, memory bloat, and capacity warnings with **specific optimization tips**. New configurable `autoMemoryDirectory` setting.

[Claude Code March 2026 Updates](https://pasqualepillitteri.it/en/news/381/claude-code-march-2026-updates)

---

### March 12 — $100M Claude Partner Network
Anthropic announced the **Claude Partner Network**, a platform for helping large enterprises adopt Claude, backed by at least **$100 million** in investment.

[Aadhunik AI Coverage](https://aadhunik.ai/blog/claude-news-march-2026/)

---

### March 11 — The Anthropic Institute
Anthropic introduced **The Anthropic Institute**, a new research arm focused on confronting societal challenges of AI. Co-founder Jack Clark leads as Head of Public Benefit.

[eWeek Coverage](https://www.eweek.com/news/anthropic-institute-launch-march-2026/)

---

### March 11 — Excel & PowerPoint Add-in Updates
Claude now provides **complete context between Excel and PowerPoint** and supports an LLM gateway connection for enterprise solutions.

[Anthropic News](https://www.anthropic.com/news)

---

### March 10 — Sydney Office
Anthropic announced **Sydney** as its fourth office in Asia-Pacific.

[Anthropic News](https://www.anthropic.com/news)

---

### March 10 — Claude Code: Voice Mode Rolling Out
The most anticipated Claude Code feature of March: **Voice Mode**. Activate with `/voice`, push-to-talk via spacebar, customizable keybindings. Not always-on listening — controlled and precise.

[Claude Code March 2026 Updates](https://pasqualepillitteri.it/en/news/381/claude-code-march-2026-updates)

---

### March 9 — Microsoft M365 Copilot Integration
Microsoft announced it will make Anthropic's latest **Claude Sonnet models available to M365 Copilot users**.

[Anthropic News](https://www.anthropic.com/news)

---

### March 6 — Mozilla Partnership
Anthropic partnered with **Mozilla to improve Firefox's security** using Claude.

[Anthropic News](https://www.anthropic.com/news)

---

## Claude Code Bonus: VS Code Overhaul
Throughout early-to-mid March, Claude Code also shipped:
- Spark icon in VS Code activity bar listing all sessions
- Sessions open as full editors
- Full markdown document view for plans with comment support
- Native MCP server management dialog (`/mcp` in chat panel)
- Remote Control `/poll` rate reduced ~300x (once per 10 min while connected)
- Non-ASCII clipboard fixes (CJK, emoji, RTL text)
- Hyperlink double-open fix in VS Code/Cursor

[Claude Code Releases](https://github.com/anthropics/claude-code/releases)

---

## By The Numbers

| Metric | Value |
|--------|-------|
| Days covered | 10 business days |
| Major platform releases | 6+ |
| Claude Code versions shipped | ~13 (v2.1.63 → v2.1.76) |
| New API features | 4+ |
| New partnerships/initiatives | 4 |
| Context window | 200K → 1M (GA, standard pricing) |
| Investment announced | $100M (Partner Network) |

---

## The Vibe

Quartz summed it up best: **"Anthropic is having a huge 2026. It's only March."**

Revenue reportedly approaching **$20 billion** annualized. Claude Code went mega viral on X. And oh yeah — **Claude 5 leaks** (codenamed "Fennec") have already appeared in Google Vertex AI logs.

The cycle never stops. You are here. →

---

*Sources: [Anthropic News](https://www.anthropic.com/news) | [Claude Platform Release Notes](https://platform.claude.com/docs/en/release-notes/overview) | [Claude Code Changelog](https://code.claude.com/docs/en/changelog) | [Claude Code GitHub Releases](https://github.com/anthropics/claude-code/releases) | [Quartz](https://qz.com/anthropic-claude-ai-business-revenue-pentagon-openai-chatgpt) | [WebProNews](https://www.webpronews.com/anthropics-march-2026-claude-promotion-what-you-need-to-know-about-the-free-usage-boost/) | [eWeek](https://www.eweek.com/news/anthropic-institute-launch-march-2026/) | [Aadhunik AI](https://aadhunik.ai/blog/claude-news-march-2026/)*
