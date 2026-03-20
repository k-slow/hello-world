# Claude Has Been INSANELY Busy

**An AI Boss Newsletter — March 20, 2026**

---

Claude has been insanely busy.

I feel like there's a new release every day — sometimes multiple a day. If you blinked this month, you missed 5 announcements. In the last 10 business days alone, Anthropic shipped **28+ releases** across products, platform, partnerships, and research.

Here's everything Anthropic shipped. Buckle up.

---

## The Releases (March 6–20, 2026)

### March 18 — Cowork Dispatch (Persistent Agent Thread)
Pro and Max users can now control the Claude Cowork agent on desktop **remotely via the Claude mobile app**. Single persistent conversation thread across all your devices. Think: start a task on your laptop, monitor it from your phone.

[COEY Coverage](https://coey.com/resources/blog/2026/03/17/anthropic-dispatch-turns-claude-into-your-always-on-creative-coworker/)

---

### March 18 — Model Capability API Fields
Anthropic added `max_input_tokens`, `max_tokens`, and a `capabilities` object to the Models API. Query the API to discover exactly what each model supports — no more guessing.

[API Release Notes](https://platform.claude.com/docs/en/release-notes/overview)

---

### March 18 — Largest AI User Study Ever Published
Anthropic published results from a study where they invited Claude.ai users to share how they use AI. Nearly **81,000 people** participated across 159 countries and 70 languages — the largest and most multilingual qualitative study of its kind.

[Anthropic on X](https://x.com/AnthropicAI/status/2034302152945144166) | [Anthropic News](https://www.anthropic.com/news)

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

[WebProNews](https://www.webpronews.com/anthropics-march-2026-claude-promotion-what-you-need-to-know-about-the-free-usage-boost/) | [Android Headlines](https://www.androidheadlines.com/2026/03/claude-double-usage-limits-march-2026-promotion.html) | [Claude Help Center](https://support.claude.com/en/articles/14063676-claude-march-2026-usage-promotion)

---

### March 14 — Claude Code: MCP Elicitation & More
Massive Claude Code update:
- **MCP Elicitation Support** — MCP servers can now request structured input mid-task via interactive dialog
- New Elicitation and ElicitationResult hooks
- `-n / --name` CLI flag for startup
- `worktree.sparsePaths` for large monorepos
- PostCompact hook
- `/effort` command (three tiers + "ultrathink" keyword)
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
- `/loop` command for recurring automated tasks
- Session name on the prompt bar
- Memory freshness timestamps
- Hook sources now visible
- Voice mode fixes
- macOS speedup

[Claude Code Changelog](https://code.claude.com/docs/en/changelog) | [Claude Code Updates](https://pasqualepillitteri.it/en/news/381/claude-code-march-2026-updates)

---

### March 12 — Inline Visualizations (Beta)
Claude can now generate **interactive charts, diagrams, timelines, and visualizations directly inline** in its responses using HTML and SVG. Unlike Artifacts, these are temporary and evolve with the conversation. Enabled by default on all plans.

[Digital Trends](https://www.digitaltrends.com/computing/claudes-responses-get-interactive-inline-visuals-to-help-you-understand-complex-topics-faster/) | [Inc.](https://www.inc.com/ben-sherry/claudes-new-visual-tools-could-make-learning-on-the-job-faster-than-ever/91315811)

---

### March 12 — Claude Code: Actionable Context Suggestions
Claude Code now identifies context-heavy tools, memory bloat, and capacity warnings with **specific optimization tips**. New configurable `autoMemoryDirectory` setting.

[Claude Code Updates](https://pasqualepillitteri.it/en/news/381/claude-code-march-2026-updates)

---

### March 12 — $100M Claude Partner Network
Anthropic announced the **Claude Partner Network**, a platform for helping large enterprises adopt Claude, backed by at least **$100 million** in investment.

[Aadhunik AI](https://aadhunik.ai/blog/claude-news-march-2026/)

---

### March 11 — The Anthropic Institute
Anthropic introduced **The Anthropic Institute**, a new research arm with three teams: Frontier Red Team (stress-testing AI), Societal Impacts, and Economic Research (AI's impact on jobs). Co-founder Jack Clark leads as Head of Public Benefit.

[eWeek](https://www.eweek.com/news/anthropic-institute-launch-march-2026/) | [Time](https://time.com/article/2026/03/11/anthropic-claude-disruptive-company-pentagon/)

---

### March 11 — Excel & PowerPoint Add-in Updates
Claude now provides **complete context between Excel and PowerPoint**. Excel add-in updated to Opus 4.6 with native operations (pivot tables, conditional formatting). Supports LLM gateway connectivity (Bedrock, Vertex AI, Foundry).

[Anthropic News](https://www.anthropic.com/news)

---

### March 10 — Sydney Office
Anthropic announced **Sydney** as its fourth office in Asia-Pacific (joining Tokyo, Bengaluru, Seoul). Australia ranks 4th globally in Claude usage relative to population.

[Anthropic News](https://www.anthropic.com/news/sydney-fourth-office-asia-pacific) | [Bloomberg](https://www.bloomberg.com/news/articles/2026-03-10/anthropic-expands-into-australia-new-zealand-with-sydney-office)

---

### March 10 — Claude Code: Voice Mode Rolling Out
The most anticipated Claude Code feature of March: **Voice Mode**. Activate with `/voice`, push-to-talk via spacebar, customizable keybindings via `keybindings.json`. Currently rolling out progressively (~5% of users).

[Claude Code Updates](https://pasqualepillitteri.it/en/news/381/claude-code-march-2026-updates)

---

### March 9 — Code Review for Claude Code (Research Preview)
**Multi-agent code review system** for Team and Enterprise plans. When a PR is opened on GitHub, multiple specialized agents analyze the code in parallel for logic errors, boundary conditions, API misuse, and auth flaws. Cost: ~$15–25 per review, ~20 minutes. Internal results: substantive review comments went from 16% to **54%** of PRs.

[Claude Blog](https://claude.com/blog/code-review) | [TechCrunch](https://techcrunch.com/2026/03/09/anthropic-launches-code-review-tool-to-check-flood-of-ai-generated-code/) | [The Register](https://www.theregister.com/2026/03/09/anthropic_debuts_code_review/)

---

### March 9 — Microsoft Copilot Cowork (Claude in M365)
Microsoft launched **Copilot Cowork**, an enterprise AI agent built on Claude, making Claude Sonnet models available to M365 Copilot users as part of a new **E7 licensing tier**.

[Axios](https://www.axios.com/2026/03/09/microsoft-copilot-cowork-anthropic) | [GeekWire](https://www.geekwire.com/2026/microsofts-new-copilot-cowork-integrates-anthropics-claude-in-rollout-of-new-e7-licensing-tier/) | [Fortune](https://fortune.com/2026/03/09/microsoft-copilot-cowork-ai-agents-anthropic-e7-m365-saas/)

---

### March 6 — Mozilla Firefox Security Partnership
Anthropic's Frontier Red Team partnered with Mozilla. Claude Opus 4.6 discovered **22 security vulnerabilities** (14 high-severity) in Firefox over two weeks, plus 90 additional bugs. Claude also generated a working exploit for one patched CVE.

[Anthropic Blog](https://www.anthropic.com/news/mozilla-firefox-security) | [TechCrunch](https://techcrunch.com/2026/03/06/anthropics-claude-found-22-vulnerabilities-in-firefox-over-two-weeks/) | [red.anthropic.com](https://red.anthropic.com/2026/firefox/)

---

### March 6 — Claude Marketplace Launch (Limited Preview)
An **Amazon-style B2B marketplace** where enterprise customers can purchase third-party Claude-powered software (Snowflake, GitLab, Harvey, Replit, Rogo, Lovable) using existing Anthropic spend commitments. No commission taken.

[VentureBeat](https://venturebeat.com/technology/anthropic-launches-claude-marketplace-giving-enterprises-access-to-claude) | [Bloomberg](https://www.bloomberg.com/news/articles/2026-03-06/anthropic-unveils-amazon-inspired-marketplace-for-ai-software)

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
- Default max output tokens bumped to 64k; upper bound to 128k for Opus 4.6

[Claude Code Releases](https://github.com/anthropics/claude-code/releases)

---

## Also Shipped (Broader March Window)

- **Alignment Science: Automated Alignment Agent (A3)** — agentic framework that automatically mitigates LLM safety failures | [Alignment Blog](https://alignment.anthropic.com/)
- **AuditBench** — benchmark of 56 LLMs with implanted hidden behaviors for evaluating alignment auditing | [Alignment Blog](https://alignment.anthropic.com/)
- **Plugin Marketplace & Admin Controls** for Team/Enterprise plans | [GitHub](https://github.com/anthropics/claude-plugins-official)
- **Haiku 3 deprecation announced** (retirement: April 19, 2026) | [Model Deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- **Sonnet 3.7 & Haiku 3.5 officially retired** — all API requests now return errors | [Model Deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)

---

## By The Numbers

| Metric | Value |
|--------|-------|
| Days covered | 10 business days |
| Total releases/announcements | 28+ |
| Claude Code versions shipped | ~13 (v2.1.63 → v2.1.76) |
| New API features | 6+ |
| New partnerships/integrations | 5 (Mozilla, Microsoft, Partner Network, Marketplace, Sydney) |
| Context window | 200K → 1M (GA, standard pricing) |
| Investment announced | $100M (Partner Network) |
| Firefox vulns found by Claude | 22 (14 high-severity) |
| User study participants | 81,000 across 159 countries |

---

## The Vibe

Quartz summed it up best: **["Anthropic is having a huge 2026. It's only March."](https://qz.com/anthropic-claude-ai-business-revenue-pentagon-openai-chatgpt)**

Revenue reportedly approaching **$20 billion** annualized. Claude Code went [mega viral on X](https://x.com/milesdeutscher/status/2012237674409796036). And oh yeah — **Claude 5 leaks** (codenamed "Fennec") have already appeared in Google Vertex AI logs with coding capabilities that reportedly surpass Opus 4.6.

The cycle never stops. You are here. →

---

*Sources: [Anthropic News](https://www.anthropic.com/news) | [Claude Platform Release Notes](https://platform.claude.com/docs/en/release-notes/overview) | [Claude Code Changelog](https://code.claude.com/docs/en/changelog) | [Claude Code GitHub Releases](https://github.com/anthropics/claude-code/releases) | [Quartz](https://qz.com/anthropic-claude-ai-business-revenue-pentagon-openai-chatgpt) | [TechCrunch](https://techcrunch.com/2026/03/06/anthropics-claude-found-22-vulnerabilities-in-firefox-over-two-weeks/) | [TechCrunch](https://techcrunch.com/2026/03/09/anthropic-launches-code-review-tool-to-check-flood-of-ai-generated-code/) | [Axios](https://www.axios.com/2026/03/09/microsoft-copilot-cowork-anthropic) | [VentureBeat](https://venturebeat.com/technology/anthropic-launches-claude-marketplace-giving-enterprises-access-to-claude) | [Digital Trends](https://www.digitaltrends.com/computing/claudes-responses-get-interactive-inline-visuals-to-help-you-understand-complex-topics-faster/) | [eWeek](https://www.eweek.com/news/anthropic-institute-launch-march-2026/) | [Time](https://time.com/article/2026/03/11/anthropic-claude-disruptive-company-pentagon/) | [WebProNews](https://www.webpronews.com/anthropics-march-2026-claude-promotion-what-you-need-to-know-about-the-free-usage-boost/) | [Fast Company](https://www.fastcompany.com/91477813/claude-cowork-is-here-and-so-are-the-memes) | [Aadhunik AI](https://aadhunik.ai/blog/claude-news-march-2026/) | [Bloomberg](https://www.bloomberg.com/news/articles/2026-03-06/anthropic-unveils-amazon-inspired-marketplace-for-ai-software)*
