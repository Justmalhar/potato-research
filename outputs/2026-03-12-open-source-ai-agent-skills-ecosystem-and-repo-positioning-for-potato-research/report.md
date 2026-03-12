# Research Report: Open-source AI agent skills ecosystem and repo positioning for potato-research

**Topic:** Open-source AI agent skills ecosystem and repo positioning for potato-research  
**Prepared for:** Open source users  
**Prepared on:** 2026-03-12  
**Depth:** Detailed  
**Status:** Final

## Executive Summary

- **Core conclusion:** `potato-research` should be positioned as an open-source, markdown-first research system with a portable agent skill and a public report archive under `outputs/`.
- The market for reusable agent skills is real and maturing: OpenAI documents Codex skills as first-class reusable workflow units, Anthropic maintains a public skills repository, and community aggregators now curate hundreds of cross-agent skills.
- The strongest differentiation is **not** “AI writes reports.” That is commodity now. The differentiation is: **structured research workflow + reusable skill + publishable markdown outputs + PDF path**.
- A GitHub-native distribution model is strategically correct because markdown renders well, version history is visible, and users can adopt either the source skill folder or packaged `.skill` artifact.
- The best positioning language is closer to **“research operating system”** or **“research lab”** than “prompt pack.” Buyers and builders care about repeatability, source quality, and output structure.
- The repo should explicitly support **OpenClaw, Claude, Codex, and adjacent agent runtimes** while being honest that small metadata/path adjustments may be needed across ecosystems.
- The canonical artifact should remain **Markdown**, with **HTML/PDF as derived outputs**. This maximizes portability and minimizes format fragility.
- The repo should include both: (1) **skill source** for inspection and adaptation, and (2) **packaged skill artifact** for drop-in installation where supported.
- Near-term upside: become a reference repo for “consulting-style research with agents.” Near-term risk: sounding generic or overclaiming “McKinsey-like” quality without enough examples.

## Key Questions

1. Is there a real open-source ecosystem for reusable AI agent skills?
2. How should `potato-research` be packaged so people can use it with OpenClaw, Claude, Codex, and similar tools?
3. What repo structure and documentation best support adoption?
4. What positioning is credible and differentiated in a crowded AI tooling market?

## Methodology

- **Scope:** Public documentation and repositories related to agent skills, cross-agent compatibility, and consulting-style report structure.
- **Time horizon:** Current ecosystem snapshot as of 2026-03-12.
- **Sources reviewed:** OpenAI Codex Skills documentation, Anthropic public skills repository, community agent skill directories, and consulting/report-structure references.
- **Inclusion criteria:** Publicly inspectable sources with direct relevance to skill packaging, distribution, or research-report structuring.
- **Known gaps / limitations:** This is a rapid strategic research brief, not a census of every skill ecosystem. Community repositories evolve quickly.

## Findings

### 1. Market / Context

Reusable agent skills are now a recognizable product category rather than a fringe pattern.

OpenAI documents Codex skills as reusable packages containing `SKILL.md` plus optional `scripts/`, `references/`, and `assets/`. Anthropic maintains a public skills repository for Claude. Community aggregators now catalog large cross-agent skill collections and explicitly market compatibility across multiple runtimes.

This means `potato-research` is entering a market with:
- clear user demand for reusable agent workflows
- emerging conventions around skill packaging
- increasing appetite for open repositories that can be inspected before install

### 2. Demand Signals

The demand signal is strongest among:
- developers using coding agents
- operators and founders doing fast market research
- people who want repeatable output formats rather than one-off chat responses
- users who prefer GitHub-native workflows and versioned deliverables

The ecosystem evidence suggests users increasingly want:
- installable skill directories
- open repositories with transparent source
- portable instructions across agent runtimes
- practical artifacts rather than abstract prompting advice

### 3. Competitive Landscape

The competitive set has three layers:

#### A. Official ecosystem repositories
- OpenAI’s Codex skills documentation establishes the packaging model and legitimizes skills as a native primitive.
- Anthropic’s public skills repository demonstrates that vendors themselves expect skills to be shared openly.

#### B. Community aggregators
- Repositories such as VoltAgent’s agent-skills collection aggregate hundreds of skills and emphasize cross-runtime compatibility.
- These repositories increase discovery but also raise the bar: low-quality “prompt dumps” get drowned out.

#### C. Adjacent research tooling
Most AI research tools stop at “generate a report.” Fewer provide:
- a reusable agent skill
- a public repo for inspection and forking
- markdown-first outputs with versioning
- a practical PDF path

That gap is the opening.

### 4. Technical / Operational Considerations

The best technical shape for this repo is:
- `skills/research-report/` for the inspectable source skill
- `packages/research-report.skill` for packaged installs
- `outputs/` for generated reports
- a README that explains both the research workflow and cross-agent installation patterns

Why this works:
- source is inspectable
- packaging is convenient
- outputs are visible and useful as examples
- GitHub becomes both distribution channel and content library

Markdown should remain canonical because:
- GitHub renders it natively
- diffs are clean
- it is easy to adapt into docs, blogs, wikis, and PDFs
- it avoids getting trapped in brittle binary formats

### 5. Economics / Business Model

Open source does not directly monetize the repo, but it can create leverage through:
- reputation and discoverability
- portfolio proof of quality
- lead generation for custom research workflows or consulting
- premium variants later: vertical templates, automation, data connectors, source packs, hosted report generation

A useful framing:
- **open core content layer:** public skill + public example reports
- **future monetizable layer:** premium templates, enterprise workflows, hosted pipelines, or bespoke research packs

## Analysis

### What seems true

- The skill ecosystem is sufficiently real to justify publishing this as an open-source repo.
- The repo should optimize for trust and inspectability, not just convenience.
- “Markdown-first, PDF-optional” is the right systems decision.
- The combination of **skill + outputs + examples** is much stronger than shipping only a skill file.
- The strongest adoption hook is practical utility: “give topic, get structured report.”

### What is uncertain

- Whether “McKinsey-like” attracts the right audience or creates avoidable skepticism.
- How much exact compatibility can be promised across OpenClaw, Claude, Codex, and other runtimes without runtime-specific install guides.
- Whether users will care more about the skill itself or the growing archive of published research outputs.

### What would change the conclusion

- If agent runtimes converge on a stronger, universal skill spec, repo structure can become even more standardized.
- If PDF demand proves materially higher than expected, a stronger automated export pipeline may be worth adding.
- If public example reports drive more adoption than the skill, the repo may evolve into a hybrid “skill + public research archive” brand.

## Risks / Counterarguments

- **Risk 1: Generic positioning.** “AI research reports” is a crowded phrase. Without sharp examples, the repo can sound interchangeable.
- **Risk 2: Overclaim risk.** “McKinsey-like” implies a quality bar. If examples are weak, the tagline becomes self-inflicted sabotage.
- **Risk 3: Cross-agent compatibility drift.** Skill formats are similar but not perfectly identical across all ecosystems.

## Recommendations

### Immediate Actions

- Publish the repo with a clear structure: `skills/`, `packages/`, and `outputs/`.
- Add installation instructions for OpenClaw, Claude-style setups, and Codex/generic agent workflows.
- Include at least one real report in `outputs/` so the repo demonstrates, rather than merely claims.
- Keep markdown as the canonical deliverable and document PDF as a derived export path.

### Next Research Steps

- Benchmark 5-10 public research/report repos and compare positioning, stars, structure, and examples.
- Test the skill in at least two runtime environments and document any install differences.
- Add 2-3 high-quality public sample reports in different domains: market, technology, and business model.

### Go / No-Go View

**Go.** The open-source repo is strategically sound. The category is real, the packaging is credible, and the repo can serve both as a usable tool and as a public proof-of-work asset.

## Sources

1. [OpenAI Codex Skills](https://developers.openai.com/codex/skills/) — Documents the skill packaging model, progressive disclosure, and reusable `SKILL.md` + resources pattern.
2. [Anthropic public skills repository](https://github.com/anthropics/skills) — Confirms vendor-level support for open skills and demonstrates repo-based skill distribution.
3. [VoltAgent awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) — Shows strong community demand for curated, cross-runtime agent skill collections.
4. [Open Agent Skills standard](https://agentskills.io) — Relevant standardization reference cited by official documentation.
5. [Consulting report structure reference](https://venngage.com/blog/consulting-report-template/) — Useful secondary reference for executive-summary-first research structure.

## Appendix

### Suggested public positioning

**Short description**  
A research lab that generates structured, consulting-style reports on any topic using a portable AI agent skill for OpenClaw, Claude, Codex, and similar runtimes.

**Shorter GitHub-friendly variant**  
Markdown-first research reports + reusable AI agent skill for OpenClaw, Claude, Codex, and more.

### Suggested messaging principles

- Lead with outputs, not prompting theory.
- Show examples quickly.
- Be explicit that markdown is canonical.
- Treat PDF as export, not origin.
- Promise portability, not magical perfect compatibility.
