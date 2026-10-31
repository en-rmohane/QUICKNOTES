import docx
import re
import html
import os
import json

doc_path = r'C:/Users/ravik/.gemini/antigravity/brain/6c832a5f-5124-4ec6-a4eb-169860004e68/.user_uploaded/media_1793461692787_471f8427.docx'
doc = docx.Document(doc_path)

def sanitize_text(text):
    if not text:
        return ""
    # Complete removal/replacement of author references
    text = re.sub(r'Dr\.?\s*R\.?\s*Nageswara\s*Rao', 'Core Python Reference', text, flags=re.IGNORECASE)
    text = re.sub(r'R\.?\s*Nageswara\s*Rao', 'Core Python Reference', text, flags=re.IGNORECASE)
    text = re.sub(r'Nageswara\s*Rao', 'Author Reference', text, flags=re.IGNORECASE)
    text = re.sub(r'nageswara\.r@rediffmail\.com', 'user@example.com', text, flags=re.IGNORECASE)
    text = re.sub(r'nageswara', 'developer', text, flags=re.IGNORECASE)
    # Quotes and unicode symbols
    text = text.replace('\u2018', "'").replace('\u2019', "'")
    text = text.replace('\u201c', '"').replace('\u201d', '"')
    text = text.replace('\u2013', '-').replace('\u2014', '--')
    text = text.replace('\ufffd', "'")
    return text

def extract_table_html(tbl_elem):
    rows = tbl_elem.xpath('.//w:tr')
    if not rows:
        return ""
    html_out = ['<div class="custom-table-container"><table class="styled-table">']
    for r_idx, row in enumerate(rows):
        cells = row.xpath('.//w:tc')
        cell_texts = []
        for cell in cells:
            p_texts = []
            for p in cell.xpath('.//w:p'):
                t = ''.join(p.xpath('.//w:t/text()')).strip()
                if t:
                    p_texts.append(sanitize_text(t))
            cell_texts.append('<br>'.join(html.escape(t) for t in p_texts))
        if r_idx == 0:
            html_out.append('<thead><tr>')
            for c in cell_texts:
                html_out.append(f'<th>{c}</th>')
            html_out.append('</tr></thead><tbody>')
        else:
            html_out.append('<tr>')
            for c in cell_texts:
                html_out.append(f'<td>{c}</td>')
            html_out.append('</tr>')
    html_out.append('</tbody></table></div>')
    return '\n'.join(html_out)

def get_paragraph_info(p_elem, doc_part):
    # Direct runs
    direct_runs = []
    for child in p_elem.iter():
        if child.tag.endswith('}r'):
            curr = child.getparent()
            in_txbx = False
            while curr is not None and curr is not p_elem:
                if curr.tag.endswith('txbxContent'):
                    in_txbx = True
                    break
                curr = curr.getparent()
            if not in_txbx:
                t_nodes = [t.text for t in child.iter() if t.tag.endswith('}t') and t.text]
                if t_nodes:
                    direct_runs.append(''.join(t_nodes))
    direct_text = sanitize_text(''.join(direct_runs).strip())

    # Textboxes & Drop-cap
    drop_cap = ""
    code_boxes = []
    seen_boxes = set()

    for el in p_elem.iter():
        if el.tag.endswith('txbxContent'):
            lines = []
            for p2 in el.iter():
                if p2.tag.endswith('}p'):
                    l = ''.join(t.text for t in p2.iter() if t.tag.endswith('}t') and t.text)
                    if l:
                        lines.append(sanitize_text(l))
            txt = '\n'.join(lines).strip()
            if not txt:
                continue
            if len(txt) == 1 and txt.isupper() and not drop_cap:
                drop_cap = txt
            elif txt not in seen_boxes and len(txt) > 1:
                # Filter out single-word label badges
                if txt.strip() not in ('Program', 'Output', 'Input', 'Note', 'Important', 'Warning'):
                    seen_boxes.add(txt)
                    code_boxes.append(txt)

    # Images
    images = []
    for el in p_elem.iter():
        if el.tag.endswith('blip'):
            rId = el.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
            if rId and rId in doc_part.related_parts:
                target = doc_part.related_parts[rId].partname
                fname = target.split('/')[-1]
                if fname not in images:
                    images.append(fname)

    # Prepend drop cap if direct text starts with lowercase
    if drop_cap and direct_text and direct_text[0].islower():
        full_text = drop_cap + direct_text
    elif drop_cap and not direct_text:
        full_text = drop_cap
    else:
        full_text = direct_text

    return full_text, code_boxes, images

CHAPTERS_METADATA = [
    (1, "Introduction to Python", "chapter-1-introduction-to-python", 157, 388),
    (2, "Writing Our First Python Program", "chapter-2-writing-our-first-python-program", 388, 698),
    (3, "Datatypes in Python", "chapter-3-datatypes-in-python", 698, 1129),
    (4, "Operators in Python", "chapter-4-operators-in-python", 1129, 1469),
    (5, "Input and Output", "chapter-5-input-and-output", 1469, 1839),
    (6, "Control Statements", "chapter-6-control-statements", 1839, 2375),
    (7, "Arrays in Python", "chapter-7-arrays-in-python", 2375, 3406),
    (8, "Strings and Characters", "chapter-8-strings-and-characters", 3406, 3949),
    (9, "Functions", "chapter-9-functions", 3949, 4657),
    (10, "Lists and Tuples", "chapter-10-lists-and-tuples", 4657, 5313),
    (11, "Dictionaries", "chapter-11-dictionaries", 5313, 5568),
    (12, "Introduction to OOPs", "chapter-12-introduction-to-oops", 5568, 5737),
    (13, "Classes and Objects", "chapter-13-classes-and-objects", 5737, 6030),
    (14, "Inheritance and Polymorphism", "chapter-14-inheritance-and-polymorphism", 6030, 6439),
    (15, "Abstract Classes and Interfaces", "chapter-15-abstract-classes-and-interfaces", 6439, 6638),
    (16, "Exceptions", "chapter-16-exceptions", 6638, 6937),
    (17, "Files in Python", "chapter-17-files-in-python", 6937, 7481),
    (18, "Regular Expressions", "chapter-18-regular-expressions", 7481, 7851),
    (19, "Data Structures in Python", "chapter-19-data-structures-in-python", 7851, 8033),
    (20, "Date and Time", "chapter-20-date-and-time", 8033, 8365),
    (21, "Threads", "chapter-21-threads", 8365, 8768),
    (22, "Graphical User Interface", "chapter-22-graphical-user-interface", 8768, 9477),
    (23, "Networking in Python", "chapter-23-networking-in-python", 9477, 9816),
    (24, "Database Connectivity", "chapter-24-database-connectivity", 9816, 10342),
    (25, "Data Science Using Python", "chapter-25-data-science-using-python", 10342, 10712)
]

def build_chapter_sections(ch_num, ch_title, ch_slug, body_start, body_end):
    sections = []
    current_sec = {
        'title': 'Overview & Background',
        'is_points': False,
        'items': []
    }

    pending_program = None
    in_output = False
    pending_figure_img = None

    def flush_program():
        nonlocal pending_program, in_output
        if pending_program:
            code_str = '\n\n'.join(pending_program['code']).strip()
            out_str = '\n'.join(pending_program['output']).strip()
            current_sec['items'].append(('program', pending_program['title'], code_str, out_str))
            pending_program = None
            in_output = False

    for b_idx in range(body_start, body_end):
        child = doc.element.body[b_idx]
        if child.tag.endswith('tbl'):
            flush_program()
            tbl_html = extract_table_html(child)
            if tbl_html:
                current_sec['items'].append(('table', tbl_html))
            continue
        
        if not child.tag.endswith('p'):
            continue

        p_style = ""
        pPr = child.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pPr')
        if pPr is not None:
            pStyle = pPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pStyle')
            if pStyle is not None:
                p_style = pStyle.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', '')

        text, codes, imgs = get_paragraph_info(child, doc.part)

        # Skip preface markers at the very start of a chapter
        if b_idx - body_start < 5 and (text.upper() in (ch_title.upper(), 'CHAPTER', str(ch_num)) or not text):
            continue

        # Heading 2 -> New Major Section
        if p_style in ('Heading2', 'Heading 2'):
            flush_program()
            if current_sec['items']:
                sections.append(current_sec)
            sec_title = text.strip()
            is_points = ('points to remember' in sec_title.lower())
            current_sec = {
                'title': sec_title,
                'is_points': is_points,
                'items': []
            }
            continue

        # Heading 3 -> Subsection heading
        if p_style in ('Heading3', 'Heading 3'):
            flush_program()
            current_sec['items'].append(('subheading', text.strip()))
            continue

        # Images
        if imgs:
            for img in imgs:
                pending_figure_img = img

        # Figure caption
        if re.match(r'^Figure\s*[\d\.]*[:\.]', text, re.IGNORECASE):
            flush_program()
            img_to_use = pending_figure_img
            pending_figure_img = None
            current_sec['items'].append(('figure', img_to_use, text.strip()))
            continue

        # Program Title
        prog_match = re.match(r'^(Program\s+\d+[:\.].*)', text, re.IGNORECASE)
        if prog_match:
            flush_program()
            pending_program = {
                'title': prog_match.group(1).strip(),
                'code': [],
                'output': []
            }
            in_output = False
            if codes:
                pending_program['code'].extend(codes)
            continue

        # Output label
        if re.match(r'^Output\s*[:\.]?\s*$', text, re.IGNORECASE) and pending_program:
            in_output = True
            if codes:
                pending_program['output'].extend(codes)
                in_output = False
            continue

        # Code textboxes
        if codes:
            if pending_program:
                if in_output:
                    pending_program['output'].extend(codes)
                    in_output = False
                else:
                    pending_program['code'].extend(codes)
            else:
                for c in codes:
                    current_sec['items'].append(('code', c))

        # List Paragraph
        if p_style in ('ListParagraph', 'List Paragraph'):
            flush_program()
            if text:
                current_sec['items'].append(('list_item', text))
            continue

        # Regular text paragraph
        if text:
            if pending_program and in_output:
                pending_program['output'].append(text)
                in_output = False
            else:
                flush_program()
                current_sec['items'].append(('paragraph', text))

    flush_program()
    if current_sec['items']:
        sections.append(current_sec)

    return sections

def render_section_html(sec, sec_idx):
    if sec['is_points']:
        items_html = []
        for it in sec['items']:
            if it[0] == 'list_item':
                items_html.append(f'<li><span class="check-icon">✓</span><div class="point-text">{it[1]}</div></li>')
            elif it[0] == 'paragraph':
                items_html.append(f'<p class="points-intro">{it[1]}</p>')
        return f'''
    <div class="points-to-remember-card" id="section-{sec_idx}">
        <div class="card-header">
            <span class="header-icon">📌</span>
            <h3>{html.escape(sec['title'])}</h3>
            <span class="revision-badge">Key Takeaways & Exam Points</span>
        </div>
        <ul class="points-grid">
            {''.join(items_html)}
        </ul>
    </div>'''

    out = [f'<div class="concept-section" id="section-{sec_idx}">']
    out.append(f'<h2 class="section-title"><span class="sec-num">{sec_idx:02d}</span> {html.escape(sec["title"])}</h2>')

    idx = 0
    items = sec['items']
    while idx < len(items):
        it = items[idx]
        itype = it[0]
        if itype == 'list_item':
            list_items = []
            while idx < len(items) and items[idx][0] == 'list_item':
                list_items.append(f'<li>{items[idx][1]}</li>')
                idx += 1
            out.append(f'<ul class="concept-list">{"".join(list_items)}</ul>')
            continue
        elif itype == 'paragraph':
            out.append(f'<p class="concept-p">{it[1]}</p>')
        elif itype == 'subheading':
            out.append(f'<h3 class="subsection-title">🔹 {html.escape(it[1])}</h3>')
        elif itype == 'code':
            out.append(f'''
            <div class="code-box">
                <div class="code-header">
                    <span class="code-lang">🐍 Python / Shell</span>
                    <button class="copy-btn" onclick="copyCode(this)">📋 Copy</button>
                </div>
                <pre><code class="language-python">{html.escape(it[1])}</code></pre>
            </div>''')
        elif itype == 'program':
            title, code, output = it[1], it[2], it[3]
            out_html = ""
            if output:
                out_html = f'''
                <div class="output-container">
                    <div class="output-header">
                        <span class="terminal-dots"><span></span><span></span><span></span></span>
                        <span class="output-label">🖥️ Terminal Output</span>
                    </div>
                    <pre class="output-block">{html.escape(output)}</pre>
                </div>'''
            out.append(f'''
            <div class="program-card">
                <div class="program-header">
                    <div class="program-title-badge">
                        <span class="prog-icon">⚡</span>
                        <strong>{html.escape(title)}</strong>
                    </div>
                    <button class="copy-btn" onclick="copyCode(this)">📋 Copy</button>
                </div>
                <div class="code-container">
                    <pre><code class="language-python">{html.escape(code)}</code></pre>
                </div>
                {out_html}
            </div>''')
        elif itype == 'figure':
            img, caption = it[1], it[2]
            img_tag = f'<img src="/static/book_images/{img}" alt="{html.escape(caption)}" loading="lazy">' if img else ''
            out.append(f'''
            <div class="figure-card">
                <div class="figure-image-wrap">
                    {img_tag}
                </div>
                <div class="figure-caption">
                    <span class="figure-badge">📊 Figure</span> {html.escape(caption)}
                </div>
            </div>''')
        elif itype == 'table':
            out.append(it[1])
        idx += 1

    out.append('</div>')
    return '\n'.join(out)

def render_full_chapter(ch_num, ch_title, ch_slug, sections):
    pills = []
    subtopics = []
    for s_idx, sec in enumerate(sections, 1):
        clean_title = sec['title'].strip()
        subtopics.append(clean_title)
        short_title = clean_title if len(clean_title) < 25 else clean_title[:22] + '...'
        pills.append(f'<a href="#section-{s_idx}" class="quick-nav-pill">{s_idx:02d}. {html.escape(short_title)}</a>')

    banner_html = f'''
    <div class="board-banner">
        <div class="banner-top">
            <span class="chapter-badge">🐍 Core Python Programming</span>
            <span class="unit-badge">Chapter {ch_num}</span>
        </div>
        <h1 class="chapter-main-title">{html.escape(ch_title)}</h1>
        <p class="chapter-desc">Comprehensive line-by-line textbook reference with interactive code blocks, terminal outputs, diagrams, and revision notes.</p>
        <div class="quick-nav-bar">
            <span class="quick-nav-title">🚀 Jump to Section:</span>
            <div class="quick-nav-pills">
                {''.join(pills)}
            </div>
        </div>
    </div>'''

    body_html = [f'<div class="learning-path">', banner_html]
    for s_idx, sec in enumerate(sections, 1):
        body_html.append(render_section_html(sec, s_idx))
    body_html.append('</div>')

    return {
        'slug': ch_slug,
        'title': f'Chapter {ch_num}: {ch_title}',
        'subtopics': subtopics,
        'content': '\n'.join(body_html)
    }

def main():
    all_chapters = {}
    print("Building all 25 chapters from textbook DOCX...")
    for num, title, slug, b_start, b_end in CHAPTERS_METADATA:
        secs = build_chapter_sections(num, title, slug, b_start, b_end)
        ch_dict = render_full_chapter(num, title, slug, secs)
        all_chapters[num] = ch_dict
        print(f"  [OK] Ch {num:02d}: {title:32s} | {len(ch_dict['subtopics']):2d} subtopics | {len(ch_dict['content']):6d} bytes")

    # Group into the 5 module files
    groups = [
        ("ch_part1.py", [1, 2, 3, 4, 5]),
        ("ch_part2.py", [6, 7, 8, 9, 10, 11]),
        ("ch_part3.py", [12, 13, 14, 15, 16]),
        ("ch_part4.py", [17, 18, 19, 20, 21]),
        ("ch_part5.py", [22, 23, 24, 25])
    ]

    out_dir = "python_notes_modules"
    os.makedirs(out_dir, exist_ok=True)

    for fname, ch_nums in groups:
        lines = [
            "# -*- coding: utf-8 -*-",
            f'"""\nChapters {ch_nums[0]} to {ch_nums[-1]} - Comprehensive Textbook Notes from Core Python Programming.\n"""\n'
        ]
        for num in ch_nums:
            ch = all_chapters[num]
            lines.append(f"# Chapter {num}: {ch['title']}")
            lines.append(f"ch{num} = {{")
            lines.append(f"    'slug': {repr(ch['slug'])},")
            lines.append(f"    'title': {repr(ch['title'])},")
            lines.append(f"    'subtopics': {repr(ch['subtopics'])},")
            lines.append(f"    'content': {repr(ch['content'])}")
            lines.append("}\n")
        
        file_path = os.path.join(out_dir, fname)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"Written {file_path} ({os.path.getsize(file_path)} bytes)")

if __name__ == '__main__':
    main()
