"""
Convert ARCHITECTURE.md to shareable HTML (can be printed to PDF from browser)
"""
import sys
import io

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import markdown
from pathlib import Path

# Paths
brain_dir = Path(r"C:\Users\AnayJoshi28\.gemini\antigravity\brain\700f9858-2d31-47ae-a83b-2f63f364e770")
md_file = brain_dir / "ARCHITECTURE.md"
project_dir = Path(r"c:\Users\AnayJoshi28\Desktop\Projects\AISSMS Main Project\Project2")
output_html = project_dir / "Research_Compass_Architecture.html"

print(f"Reading markdown from: {md_file}")

# Read markdown
with open(md_file, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert markdown to HTML
md = markdown.Markdown(extensions=[
    'extra',      # Tables, fenced code blocks
    'codehilite', # Syntax highlighting
    'toc',        # Table of contents
])
html_body = md.convert(md_content)

# Create full HTML document with professional styling
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Research Compass - Architecture Documentation</title>
    <style>
        /* Print-friendly styling */
        @media print {{
            body {{
                margin: 0;
                padding: 20px;
            }}
            .no-print {{
                display: none;
            }}
            h1, h2, h3 {{
                page-break-after: avoid;
            }}
            pre, table {{
                page-break-inside: avoid;
            }}
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Arial, sans-serif;
            line-height: 1.7;
            color: #2c3e50;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px 20px;
        }}
        
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            padding: 60px;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }}
        
        .title-page {{
            text-align: center;
            padding: 80px 0;
            border-bottom: 3px solid #667eea;
            margin-bottom: 60px;
        }}
        
        .title-page h1 {{
            font-size: 48px;
            color: #667eea;
            margin-bottom: 20px;
            font-weight: 700;
        }}
        
        .title-page .subtitle {{
            font-size: 24px;
            color: #34495e;
            font-weight: 600;
            margin-bottom: 10px;
        }}
        
        .title-page .description {{
            font-size: 16px;
            color: #7f8c8d;
            margin: 20px 0;
        }}
        
        .title-page .meta {{
            font-size: 14px;
            color: #95a5a6;
            margin-top: 30px;
        }}
        
        h1 {{
            color: #667eea;
            font-size: 36px;
            margin: 40px 0 20px 0;
            border-bottom: 3px solid #667eea;
            padding-bottom: 12px;
            font-weight: 700;
        }}
        
        h2 {{
            color: #764ba2;
            font-size: 28px;
            margin: 35px 0 15px 0;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 10px;
            font-weight: 600;
        }}
        
        h3 {{
            color: #34495e;
            font-size: 22px;
            margin: 25px 0 12px 0;
            font-weight: 600;
        }}
        
        h4 {{
            color: #555;
            font-size: 18px;
            margin: 20px 0 10px 0;
            font-weight: 600;
        }}
        
        p {{
            margin: 15px 0;
            text-align: justify;
        }}
        
        code {{
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 3px 8px;
            border-radius: 4px;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            font-size: 0.9em;
            color: #e74c3c;
            border: 1px solid #dee2e6;
        }}
        
        pre {{
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: #ecf0f1;
            border: 1px solid #34495e;
            border-left: 5px solid #667eea;
            padding: 20px;
            border-radius: 6px;
            overflow-x: auto;
            margin: 20px 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        pre code {{
            background: transparent;
            color: #ecf0f1;
            padding: 0;
            border: none;
            font-size: 0.9em;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        thead {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }}
        
        th {{
            padding: 15px;
            text-align: left;
            color: white;
            font-weight: 600;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid #ecf0f1;
        }}
        
        tr:nth-child(even) {{
            background-color: #f8f9fa;
        }}
        
        tr:hover {{
            background-color: #e9ecef;
        }}
        
        ul, ol {{
            margin: 15px 0 15px 30px;
        }}
        
        li {{
            margin: 8px 0;
            line-height: 1.6;
        }}
        
        blockquote {{
            border-left: 5px solid #f39c12;
            background: linear-gradient(to right, #fef9e7 0%, #fcf3cf 100%);
            padding: 15px 20px;
            margin: 20px 0;
            border-radius: 4px;
        }}
        
        a {{
            color: #667eea;
            text-decoration: none;
            border-bottom: 1px dotted #667eea;
            transition: all 0.3s ease;
        }}
        
        a:hover {{
            color: #764ba2;
            border-bottom: 1px solid #764ba2;
        }}
        
        hr {{
            border: none;
            border-top: 2px solid #ecf0f1;
            margin: 40px 0;
        }}
        
        strong {{
            color: #2c3e50;
            font-weight: 600;
        }}
        
        .print-button {{
            position: fixed;
            top: 30px;
            right: 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 30px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            transition: all 0.3s ease;
            z-index: 1000;
        }}
        
        .print-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
        }}
        
        .badge {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
            margin: 0 5px;
        }}
        
        .badge-primary {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }}
        
        /* Emoji support */
        .emoji {{
            font-size: 1.2em;
        }}
    </style>
</head>
<body>
    <button class="print-button no-print" onclick="window.print()">🖨️ Print to PDF</button>
    
    <div class="container">
        <div class="title-page">
            <h1>🧠 Research Compass</h1>
            <div class="subtitle">Multi-Agent RAG System</div>
            <div class="description">
                <strong>Complete Architecture Documentation</strong><br>
                Progressive Knowledge Base • AI-Powered Research Assistant
            </div>
            <div class="meta">
                <span class="badge badge-primary">Version 1.0</span>
                <span class="badge badge-primary">January 2026</span>
            </div>
        </div>
        
        {html_body}
        
        <hr>
        <div style="text-align: center; color: #95a5a6; margin-top: 60px; padding: 20px;">
            <p><strong>Research Compass</strong> - Multi-Agent RAG System</p>
            <p style="font-size: 14px;">Built with Flask, Groq AI, and Progressive Knowledge Base Architecture</p>
        </div>
    </div>
    
    <script>
        // Add smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{ behavior: 'smooth' }});
                }}
            }});
        }});
    </script>
</body>
</html>
"""

# Write HTML file
with open(output_html, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"✅ HTML file created successfully!")
print(f"📄 Output: {output_html}")
print(f"📦 File size: {output_html.stat().st_size / 1024:.1f} KB")
print("\n📌 Instructions to create PDF:")
print("   1. Open the HTML file in your browser")
print("   2. Click the 'Print to PDF' button (or Ctrl+P)")
print("   3. Select 'Save as PDF' as the printer")
print("   4. Click 'Save'")
print("\n✨ The HTML file is also shareable directly - it looks great in any browser!")
