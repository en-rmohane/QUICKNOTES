# -*- coding: utf-8 -*-
"""
Generator script to produce python_programming_notes.md
"""
from python_data import python_data
import re

def html_to_markdown(html_text):
    text = html_text
    # Remove board banner wrapper
    text = re.sub(r'<div class="board-banner"[^>]*>.*?<h1[^>]*>(.*?)</h1>.*?<p[^>]*>(.*?)</p>.*?</div>', r'# \1\n\n>\2\n\n', text, flags=re.DOTALL)
    # Convert headings
    text = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n', text)
    text = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', text)
    text = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n', text)
    # Convert code blocks
    text = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', lambda m: f"```python\n{m.group(1).replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')}\n```\n", text, flags=re.DOTALL)
    # Convert inline code
    text = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', text)
    # Convert bold / em
    text = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', text)
    text = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', text)
    # Convert unordered lists
    text = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', text)
    text = re.sub(r'<ul[^>]*>', r'\n', text)
    text = re.sub(r'</ul>', r'\n', text)
    # Convert paragraphs
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', text, flags=re.DOTALL)
    # Convert mermaid
    text = re.sub(r'<div class="mermaid"[^>]*>(.*?)</div>', lambda m: f"```mermaid\n{m.group(1).strip()}\n```\n", text, flags=re.DOTALL)
    # Strip remaining divs and cleanup
    text = re.sub(r'</?(div|span|table|thead|tbody|tr|th|td)[^>]*>', '', text)
    text = text.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&').replace('&quot;', '"')
    # Collapse excess empty lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

output_lines = [
    "# 🐍 Python Programming Master Guide: From Basic to Advanced",
    "\n*Comprehensive, Production-Grade Reference Notes covering Syntax, Internals, Data Structures, OOP, Metaprogramming, Concurrency, and Gotchas.*\n",
    "---\n",
    "## 📑 Table of Contents\n"
]

for unit in python_data:
    output_lines.append(f"- **{unit['unit']}: {unit['title']}**")
    for topic in unit['topics']:
        output_lines.append(f"  - [{topic['title']}](#{topic['slug']})")

output_lines.append("\n---\n")

for unit in python_data:
    output_lines.append(f"\n# {unit['unit']}: {unit['title']}\n")
    for topic in unit['topics']:
        output_lines.append(f"<a id=\"{topic['slug']}\"></a>\n")
        output_lines.append(f"## {topic['title']}\n")
        output_lines.append(f"**Topics Covered:** {', '.join(topic['subtopics'])}\n")
        output_lines.append(html_to_markdown(topic['content']))
        output_lines.append("\n\n---\n")

with open("python_programming_notes.md", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print("Successfully generated python_programming_notes.md!")
