# Personal brand workspace

This is the working directory for your personal brand build. Every artifact the agent system produces lands here.

## How to use it

From Claude Code, run:

```
/brand
```

That launches the orchestrator. It will read `STATE.md` (or create it on first run), figure out the next best step, and either interview you or hand off to a specialist.

You can also pass intent:

```
/brand let's work on the funnel today
/brand I just recorded a new YouTube video, run the waterfall on it
/brand find me outlier patterns from this week's competitor posts
```

## The 5 stages (Donley framework)

1. **Story** — `story-miner` extracts 10+ real moments (wrong-looking decisions, sacrifices, public failures). Output: `story-bank.md`.
2. **Voice** — `voice-capturer` profiles how you actually write/speak. Output: `voice.md`. (Run early — every later agent reads this.)
3. **Pillars** — `pillar-strategist` defines 3-4 specific content topics at the overlap of what you're known for × what your audience pays for × what your offer solves. Output: `pillars.md`.
4. **Platform & cadence** — `platform-coach` picks the ONE platform to go all-in on first, with numeric exit criteria for when to add a second. Output: `platform-plan.md`.
5. **Waterfall** — `waterfall-producer` takes one long-form piece and produces ~14 derivatives (10 shortform posts + 3 video scripts + 1 newsletter). Output: `content/<slug>/`.
6. **Outliers** — `outlier-analyst` finds topics performing 5x median across 3+ competitor profiles and writes 10 pre-validated post ideas in your voice. Output: `outliers/YYYY-MM-DD.md`.
7. **Funnel** — `funnel-architect` builds the lead magnet → 5-7 email sequence → webinar that converts followers into buyers. Output: `funnel/`.

## Folder layout

```
brand/
├── README.md            (this file)
├── STATE.md             (progress, decisions, next step — orchestrator owns this)
├── profile.md           (who you are, what you sell, who you sell to)
├── story-bank.md        (raw moments — story-miner)
├── voice.md             (tone, signature phrases, banned phrases — voice-capturer)
├── pillars.md           (3-4 content pillars — pillar-strategist)
├── platform-plan.md     (chosen platform + cadence + exit criteria — platform-coach)
├── content/             (one folder per long-form source — waterfall-producer)
│   └── <slug>/
│       ├── 00-source.md
│       ├── 01-shortform/
│       ├── 02-video-scripts/
│       ├── 03-newsletter.md
│       └── index.md
├── outliers/            (competitor pattern analyses — outlier-analyst)
└── funnel/              (lead magnet + email sequence + webinar — funnel-architect)
    ├── 01-lead-magnet.md
    ├── 02-email-sequence.md
    ├── 03-webinar.md
    └── index.md
```

## Hard principles baked into the agents

- Saves and shares matter, likes and views don't.
- One platform until traction is consistent. Then expand.
- Every pillar must bridge cleanly to the offer.
- Stories must be specific (date, person, number, room) — generic = cut.
- Failures stay raw. Sanitized failures don't build trust.
- Voice profile is sacred — every output is checked against `voice.md` banned phrases.
