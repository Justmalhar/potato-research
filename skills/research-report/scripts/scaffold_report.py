#!/usr/bin/env python3
import argparse
import datetime as dt
import pathlib
import re


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "research-report"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a research report folder from the skill template.")
    parser.add_argument("topic", help="Research topic")
    parser.add_argument("--audience", default="Malhar", help="Intended audience label")
    parser.add_argument("--depth", default="Detailed", help="Depth label")
    parser.add_argument("--title", default=None, help="Optional report title")
    parser.add_argument("--output-dir", default="/home/node/.openclaw/workspace/research", help="Base output directory")
    args = parser.parse_args()

    skill_dir = pathlib.Path(__file__).resolve().parents[1]
    template_path = skill_dir / "assets" / "research-report-template.md"
    template = template_path.read_text(encoding="utf-8")

    today = dt.datetime.utcnow().strftime("%Y-%m-%d")
    slug = slugify(args.topic)
    report_dir = pathlib.Path(args.output_dir) / f"{today}-{slug}"
    report_dir.mkdir(parents=True, exist_ok=True)

    title = args.title or f"Research Report: {args.topic}"
    rendered = (
        template.replace("{{TITLE}}", title)
        .replace("{{TOPIC}}", args.topic)
        .replace("{{AUDIENCE}}", args.audience)
        .replace("{{DATE}}", today)
        .replace("{{DEPTH}}", args.depth)
    )

    report_path = report_dir / "report.md"
    notes_path = report_dir / "notes.md"

    report_path.write_text(rendered, encoding="utf-8")
    if not notes_path.exists():
        notes_path.write_text("# Research Notes\n\n- Raw notes\n- Source snippets\n- Open questions\n", encoding="utf-8")

    print(report_path)


if __name__ == "__main__":
    main()
