#!/usr/bin/env python3
import argparse
import html
import pathlib
import re


def inline_format(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def markdown_to_html(md: str, title: str) -> str:
    lines = md.splitlines()
    out = []
    in_ul = False
    in_code = False
    code_lines = []

    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    for line in lines:
        if line.strip().startswith("```"):
            close_ul()
            if in_code:
                code_html = html.escape("\n".join(code_lines))
                out.append(f"<pre><code>{code_html}</code></pre>")
                code_lines = []
                in_code = False
            else:
                in_code = True
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not line.strip():
            close_ul()
            continue

        if line.startswith("### "):
            close_ul()
            out.append(f"<h3>{inline_format(line[4:].strip())}</h3>")
        elif line.startswith("## "):
            close_ul()
            out.append(f"<h2>{inline_format(line[3:].strip())}</h2>")
        elif line.startswith("# "):
            close_ul()
            out.append(f"<h1>{inline_format(line[2:].strip())}</h1>")
        elif re.match(r"^\s*[-*] ", line):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            item = re.sub(r"^\s*[-*] ", "", line)
            out.append(f"<li>{inline_format(item)}</li>")
        elif re.match(r"^\d+\. ", line):
            close_ul()
            item = re.sub(r"^\d+\. ", "", line)
            out.append(f"<p>{line.split('.',1)[0]}. {inline_format(item)}</p>")
        else:
            close_ul()
            out.append(f"<p>{inline_format(line.strip())}</p>")

    close_ul()
    if in_code:
        code_html = html.escape("\n".join(code_lines))
        out.append(f"<pre><code>{code_html}</code></pre>")

    body = "\n".join(out)
    return f"""<!doctype html>
<html>
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{html.escape(title)}</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; color: #111; line-height: 1.6; margin: 40px auto; max-width: 900px; padding: 0 24px; }}
    h1, h2, h3 {{ line-height: 1.25; }}
    h1 {{ font-size: 2.1rem; margin-top: 0; }}
    h2 {{ margin-top: 2rem; border-bottom: 1px solid #e5e7eb; padding-bottom: 0.3rem; }}
    code {{ background: #f3f4f6; padding: 0.1rem 0.3rem; border-radius: 4px; }}
    pre {{ background: #0f172a; color: #e2e8f0; padding: 16px; border-radius: 10px; overflow-x: auto; }}
    pre code {{ background: transparent; padding: 0; color: inherit; }}
    a {{ color: #2563eb; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    ul {{ padding-left: 1.3rem; }}
    @media print {{ body {{ margin: 0 auto; max-width: 100%; }} a {{ color: inherit; }} }}
  </style>
</head>
<body>
{body}
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert a markdown file into a standalone HTML file.")
    parser.add_argument("input", help="Path to markdown file")
    parser.add_argument("--output", default=None, help="Output HTML path")
    args = parser.parse_args()

    input_path = pathlib.Path(args.input)
    md = input_path.read_text(encoding="utf-8")
    title = next((line[2:].strip() for line in md.splitlines() if line.startswith("# ")), input_path.stem)
    output_path = pathlib.Path(args.output) if args.output else input_path.with_suffix(".html")
    output_path.write_text(markdown_to_html(md, title), encoding="utf-8")
    print(output_path)


if __name__ == "__main__":
    main()
