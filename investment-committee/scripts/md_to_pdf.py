import os
import sys
import markdown
from playwright.sync_api import sync_playwright

def convert_md_to_pdf(input_path, output_path, css_path=None):
    print(f"[PDF] Converting {input_path} -> {output_path}...", flush=True)
    
    # Read Markdown
    with open(input_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert to HTML
    html_body = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
    
    # Read CSS
    css_content = ""
    if css_path and os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
            
    # Create Full HTML
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            {css_content}
        </style>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """
    
    # Use Playwright to print to PDF
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html_content)
        page.pdf(path=output_path, format="A4", print_background=True, margin={"top": "20mm", "bottom": "20mm", "left": "20mm", "right": "20mm"})
        browser.close()
        
    print(f"[PDF] Success! Saved to {output_path}", flush=True)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python md_to_pdf.py <input_md> <output_pdf> [css_file]")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    css_file = sys.argv[3] if len(sys.argv) > 3 else None
    
    convert_md_to_pdf(input_file, output_file, css_file)
