"""
Convert ARCHITECTURE.md to professional PDF
"""
import markdown
from weasyprint import HTML, CSS
from pathlib import Path

# Paths
brain_dir = Path(r"C:\Users\AnayJoshi28\.gemini\antigravity\brain\700f9858-2d31-47ae-a83b-2f63f364e770")
md_file = brain_dir / "ARCHITECTURE.md"
output_pdf = Path(r"c:\Users\AnayJoshi28\Desktop\Projects\AISSMS Main Project\Project2") / "Research_Compass_Architecture.pdf"

print(f"Reading markdown from: {md_file}")

# Read markdown
with open(md_file, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert markdown to HTML
md = markdown.Markdown(extensions=[
    'extra',      # Tables, fenced code blocks
    'codehilite', # Syntax highlighting
    'toc',        # Table of contents
    'nl2br'       # Newline to break
])
html_content = md.convert(md_content)

# Create full HTML document with styling
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Research Compass - Architecture Documentation</title>
    <style>
        @page {{
            size: A4;
            margin: 2cm;
            @bottom-center {{
                content: "Page " counter(page) " of " counter(pages);
                font-size: 10px;
                color: #666;
            }}
        }}
        
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 100%;
        }}
        
        h1 {{
            color: #1a73e8;
            border-bottom: 3px solid #1a73e8;
            padding-bottom: 10px;
            margin-top: 30px;
            page-break-after: avoid;
        }}
        
        h2 {{
            color: #1a73e8;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 8px;
            margin-top: 25px;
            page-break-after: avoid;
        }}
        
        h3 {{
            color: #333;
            margin-top: 20px;
            page-break-after: avoid;
        }}
        
        h4 {{
            color: #555;
            margin-top: 15px;
        }}
        
        code {{
            background-color: #f5f5f5;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 0.9em;
            color: #d63384;
        }}
        
        pre {{
            background-color: #f8f9fa;
            border: 1px solid #e0e0e0;
            border-left: 4px solid #1a73e8;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            page-break-inside: avoid;
        }}
        
        pre code {{
            background-color: transparent;
            padding: 0;
            color: #333;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            page-break-inside: avoid;
        }}
        
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        
        th {{
            background-color: #1a73e8;
            color: white;
            font-weight: bold;
        }}
        
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        
        blockquote {{
            border-left: 4px solid #ffc107;
            background-color: #fff9e6;
            padding: 10px 20px;
            margin: 15px 0;
            page-break-inside: avoid;
        }}
        
        ul, ol {{
            margin: 10px 0;
            padding-left: 30px;
        }}
        
        li {{
            margin: 5px 0;
        }}
        
        a {{
            color: #1a73e8;
            text-decoration: none;
        }}
        
        hr {{
            border: none;
            border-top: 2px solid #e0e0e0;
            margin: 30px 0;
        }}
        
        strong {{
            color: #000;
        }}
        
        .title-page {{
            text-align: center;
            padding: 100px 0;
            page-break-after: always;
        }}
        
        .title-page h1 {{
            font-size: 48px;
            border: none;
            margin-bottom: 20px;
        }}
        
        .title-page p {{
            font-size: 18px;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="title-page">
        <h1>🧠 Research Compass</h1>
        <p><strong>Multi-Agent RAG System</strong></p>
        <p>Complete Architecture Documentation</p>
        <br><br>
        <p style="font-size: 14px; color: #999;">
            Progressive Knowledge Base • AI-Powered Research Assistant<br>
            Version 1.0 • January 2026
        </p>
    </div>
    
    {html_content}
</body>
</html>
"""

print("Converting to PDF...")

# Convert to PDF
HTML(string=html_template).write_pdf(
    output_pdf,
    stylesheets=[]
)

print(f"✅ PDF created successfully!")
print(f"📄 Output: {output_pdf}")
print(f"📦 File size: {output_pdf.stat().st_size / 1024:.1f} KB")
print("\nYou can now share this PDF with your friend!")
