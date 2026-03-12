---
name: research-report
description: Create structured research reports from a user-provided topic, question, company, market, technology, or trend. Use when the user wants a reusable research workflow, a detailed markdown report, a PDF-ready report, a research brief template, or a repo-friendly report that can be published to GitHub for reading with markdown formatting.
---

# Research Report

Create a clean, evidence-based research deliverable that can end as markdown, HTML, PDF, or a GitHub-hosted document.

## Core workflow

1. Clarify the topic, audience, and desired depth if the request is ambiguous.
2. Gather source material with web search/fetch and prioritize primary sources whenever possible.
3. Create the report in markdown using `assets/research-report-template.md` as the starting shape.
4. Save the markdown in a user-appropriate location such as `/home/node/.openclaw/workspace/research/<slug>/report.md`.
5. If the user wants a browser-friendly local preview, run `scripts/markdown_to_html.py` to create HTML.
6. If the user wants a PDF, open the generated HTML in the browser and export/print to PDF.
7. If the user wants the report pushed to GitHub, ask for the target repo if it is not already available, then commit and push only after explicit approval for the external write.

## Output rules

- Prefer markdown as the canonical source.
- Keep the report strongly structured with executive summary first.
- Distinguish facts, inferences, and recommendations.
- Include a source section with inline links or footnotes.
- Explicitly mark uncertainty, missing data, and assumptions.
- Avoid fake citations and avoid padding with generic prose.

## Template use

Start from `assets/research-report-template.md`.

Replace placeholders with the actual topic and date. Keep or delete sections based on the use case, but prefer this default order:
- title and metadata
- executive summary
- key questions
- methodology
- findings
- analysis
- risks / counterarguments
- recommendations
- sources
- appendix

## PDF path

This skill treats markdown as the source of truth.

For PDF output:
1. Convert markdown to HTML with `scripts/markdown_to_html.py`.
2. Open the HTML in the browser.
3. Use the browser PDF export to create a final PDF.

If the environment lacks a reliable PDF CLI, do not fight the machine. Produce markdown + HTML and then export with the browser.

## GitHub path

When the user prefers GitHub-readable output:
- create or update the markdown report locally first
- keep relative asset paths clean
- optionally add a short `README.md` that links to the report if the repo structure benefits from it
- commit with a specific message
- push only after explicit permission because it is an external action

## Files in this skill

- `assets/research-report-template.md` — default report scaffold
- `references/research-quality-checklist.md` — quality bar and section guidance
- `scripts/scaffold_report.py` — create a dated report folder and seed files from the template
- `scripts/markdown_to_html.py` — render a simple standalone HTML file for browser preview or PDF export

## Suggested prompts this skill should handle

- "Research the AI note-taking market and give me a report as markdown"
- "Create a detailed research report on humanoid robotics and export it as PDF"
- "Use the research template for Indian creator economy tools"
- "Research this startup idea and put the report in a GitHub repo"
- "Make me a reusable research report workflow where I only give you the topic"
