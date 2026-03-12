# potato-research

A research lab that generates **McKinsey-like reports** on any given topic, powered by a reusable **AI agent skill** compatible with **OpenClaw, Claude, Codex**, and adjacent agent setups.

## What this repo is

`potato-research` is a lightweight open-source system for topic-driven research.

You give an agent a topic such as:
- `AI agents for enterprise workflows`
- `Humanoid robotics market outlook`
- `Indian creator economy software landscape`
- `Open source alternatives to Salesforce for SMBs`

The agent produces:
- a structured **research report in Markdown**
- an optional **HTML preview**
- an optional **PDF export path**
- source-backed findings using a reusable **research-report skill**

Markdown is the canonical source of truth. GitHub renders it well, version control works naturally, and PDF can be derived when needed.

## Repo structure

```text
potato-research/
├── README.md
├── LICENSE
├── .gitignore
├── outputs/                     # generated research reports live here
│   └── README.md
├── skills/
│   └── research-report/         # reusable skill source
│       ├── SKILL.md
│       ├── assets/
│       ├── references/
│       └── scripts/
└── packages/
    └── research-report.skill    # packaged skill for OpenClaw-style installs
```

## Compatibility

This repo is designed to be useful across multiple agent environments.

### OpenClaw
Use the packaged `.skill` artifact from `packages/` or copy the raw skill folder into your local skills directory.

### Claude / Claude Code style skill setups
Copy `skills/research-report/` into your local skills collection and adapt the trigger metadata if your runtime expects a slightly different convention.

### Codex / generic agent setups
Use the raw skill folder as the reusable prompt + workflow scaffold. The markdown template and helper scripts are portable.

## Install the skill

### Option A — use the raw skill folder

Copy this directory into your agent skills collection:

```bash
skills/research-report/
```

### Option B — use the packaged skill

Use:

```bash
packages/research-report.skill
```

This is the most convenient path for setups that support packaged skills directly.

## How to use

Example prompts:

- `Research the AI note-taking market and create a detailed report`
- `Create a research report on humanoid robotics and keep it markdown-first`
- `Research Indian fintech APIs and export a PDF-ready version`
- `Research vertical AI startups in healthcare and save the output in outputs/`

## Report workflow

1. Provide a topic.
2. The agent researches the topic using web sources and primary references where possible.
3. The report is created from the reusable markdown template.
4. The final report is saved under `outputs/`.
5. Optional: convert markdown to HTML.
6. Optional: export HTML to PDF via browser print/export.

## Output conventions

All generated reports should live under `outputs/`.

Recommended pattern:

```text
outputs/
└── 2026-03-12-open-source-agent-skills/
    ├── report.md
    ├── report.html
    └── notes.md
```

This keeps the repo readable and makes each report self-contained.

## Included skill

The `research-report` skill provides:
- a structured research template
- a quality checklist
- a scaffold script for creating new reports
- a markdown-to-HTML script for clean preview and PDF export

## Design philosophy

- **Markdown-first**: best for GitHub, diffing, reuse, and portability
- **PDF-second**: useful for delivery, terrible as the source of truth
- **Primary-source bias**: prefer official docs, filings, product pages, papers, and direct company announcements
- **Decision-oriented structure**: executive summary, findings, analysis, risks, recommendations

## Example local workflow

Create a new report scaffold:

```bash
python3 skills/research-report/scripts/scaffold_report.py "AI agents for enterprise workflows" --output-dir outputs
```

Convert markdown to HTML:

```bash
python3 skills/research-report/scripts/markdown_to_html.py outputs/2026-03-12-ai-agents-for-enterprise-workflows/report.md
```

## Notes on PDF export

This repo treats PDF as a derived export.

Reliable path:
- write report in markdown
- convert to HTML
- open in browser
- export/print to PDF

That approach is boring, stable, and difficult to break — which is exactly what we want.

## Who this is for

- founders doing market research
- operators writing strategy briefs
- consultants building fast first-pass reports
- researchers who want structured markdown outputs instead of chat sludge
- agent builders who want a reusable research skill

## License

MIT
