#!/usr/bin/env python3
"""Convert homework_written.md to a printable HTML file.
Open the resulting HTML in a browser and use Ctrl+P -> Save as PDF."""

import re

def md_to_html(md_text):
    lines = md_text.split('\n')
    html_parts = []
    in_table = False
    table_rows = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Headings
        if line.startswith('# ') and not line.startswith('## '):
            if in_table:
                html_parts.append(flush_table(table_rows))
                in_table = False; table_rows = []
            html_parts.append(f'<h1>{process_inline(line[2:])}</h1>')
            i += 1; continue
        if line.startswith('## ') and not line.startswith('### '):
            if in_table:
                html_parts.append(flush_table(table_rows))
                in_table = False; table_rows = []
            html_parts.append(f'<h2>{process_inline(line[3:])}</h2>')
            i += 1; continue
        if line.startswith('### ') and not line.startswith('#### '):
            if in_table:
                html_parts.append(flush_table(table_rows))
                in_table = False; table_rows = []
            html_parts.append(f'<h3>{process_inline(line[4:])}</h3>')
            i += 1; continue
        if line.startswith('#### '):
            if in_table:
                html_parts.append(flush_table(table_rows))
                in_table = False; table_rows = []
            html_parts.append(f'<h4>{process_inline(line[5:])}</h4>')
            i += 1; continue
        
        # Horizontal rule
        if line.strip() == '---':
            if in_table:
                html_parts.append(flush_table(table_rows))
                in_table = False; table_rows = []
            html_parts.append('<hr>')
            i += 1; continue
        
        # Table rows
        if '|' in line and line.strip().startswith('|'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            # Skip separator rows
            if all(re.match(r'^[-:]+$', c) for c in cells):
                in_table = True
                i += 1; continue
            if not in_table:
                in_table = True
                table_rows.append(('header', cells))
            else:
                table_rows.append(('row', cells))
            i += 1; continue
        else:
            if in_table:
                html_parts.append(flush_table(table_rows))
                in_table = False; table_rows = []
        
        # Empty line
        if line.strip() == '':
            i += 1; continue
        
        # List items
        if line.startswith('- '):
            items = [process_inline(line[2:])]
            i += 1
            while i < len(lines) and lines[i].startswith('- '):
                items.append(process_inline(lines[i][2:]))
                i += 1
            html_parts.append('<ul>' + ''.join(f'<li>{item}</li>' for item in items) + '</ul>')
            continue
        
        # Regular paragraph
        para = [line]
        i += 1
        while i < len(lines) and lines[i].strip() != '' and not lines[i].startswith('#') and not lines[i].startswith('---') and not lines[i].startswith('|') and not lines[i].startswith('- '):
            para.append(lines[i])
            i += 1
        html_parts.append(f'<p>{process_inline(" ".join(para))}</p>')
    
    if in_table:
        html_parts.append(flush_table(table_rows))
    
    return '\n'.join(html_parts)


def flush_table(rows):
    html = '<table>'
    for rtype, cells in rows:
        tag = 'th' if rtype == 'header' else 'td'
        html += '<tr>' + ''.join(f'<{tag}>{process_inline(c)}</{tag}>' for c in cells) + '</tr>'
    html += '</table>'
    return html


def process_inline(text):
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Line breaks
    text = text.replace('  \n', '<br>')
    return text


def main():
    with open('homework_written.md', 'r', encoding='utf-8') as f:
        md = f.read()
    
    html_body = md_to_html(md)
    
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>BLG 483E – Quiz 4 Part I: Written Responses</title>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    body {{
        font-family: 'Inter', sans-serif;
        max-width: 850px;
        margin: 40px auto;
        padding: 0 20px;
        color: #222;
        line-height: 1.65;
        font-size: 11pt;
    }}
    h1 {{ font-size: 20pt; border-bottom: 2px solid #333; padding-bottom: 8px; }}
    h2 {{ font-size: 16pt; color: #1a5276; margin-top: 30px; }}
    h3 {{ font-size: 13pt; color: #2e4053; }}
    h4 {{ font-size: 11pt; color: #34495e; }}
    table {{
        border-collapse: collapse;
        width: 100%;
        margin: 15px 0;
        font-size: 10pt;
    }}
    th, td {{
        border: 1px solid #bbb;
        padding: 6px 10px;
        text-align: left;
    }}
    th {{ background: #ecf0f1; font-weight: 600; }}
    code {{
        background: #f4f4f4;
        padding: 1px 4px;
        border-radius: 3px;
        font-size: 10pt;
    }}
    hr {{ border: none; border-top: 1px solid #ccc; margin: 25px 0; }}
    p {{ margin: 8px 0; }}
    blockquote {{
        border-left: 3px solid #3498db;
        padding-left: 12px;
        margin-left: 0;
        color: #555;
    }}
    @media print {{
        body {{ margin: 20px; font-size: 10pt; }}
        h2 {{ page-break-before: auto; }}
    }}
</style>
</head>
<body>
{html_body}
</body>
</html>"""
    
    with open('homework_written.html', 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print("Created homework_written.html")
    print("Open it in a browser and press Ctrl+P -> Save as PDF")


if __name__ == '__main__':
    main()
