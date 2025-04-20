#!/usr/bin/env python3
"""
PDF to Markdown converter for OpenScope Community Project documentation.

This script extracts text and images from PDF files and converts them into
markdown files that can be used with the MkDocs site.

Usage:
    python pdf_to_markdown.py input.pdf [output_dir]

If output_dir is not provided, the script will use docs/pdf-extracts/
"""

import os
import sys
import re
import argparse
from pathlib import Path
import shutil
from datetime import datetime

try:
    import fitz  # PyMuPDF
    from PIL import Image
    import io
except ImportError:
    print("Required packages not installed. Please run:")
    print("pip install PyMuPDF Pillow")
    sys.exit(1)

DEFAULT_OUTPUT_DIR = "docs/pdf-extracts"

def sanitize_filename(filename):
    """Convert a string to a valid filename."""
    return re.sub(r'[^\w\-_.]', '_', filename)

def extract_pdf_content(pdf_path, output_dir):
    """
    Extract text and images from a PDF file and create markdown files.
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to store the generated markdown and images
    
    Returns:
        Path to the main markdown file
    """
    # Ensure output directories exist
    md_dir = os.path.join(output_dir)
    img_dir = os.path.join(output_dir, "img")
    os.makedirs(md_dir, exist_ok=True)
    os.makedirs(img_dir, exist_ok=True)
    
    # Open the PDF file
    pdf_name = os.path.basename(pdf_path)
    base_name = os.path.splitext(pdf_name)[0]
    sanitized_name = sanitize_filename(base_name)
    
    # Initialize markdown content
    md_content = f"# {base_name}\n\n"
    md_content += f"*Generated from PDF on {datetime.now().strftime('%Y-%m-%d')}*\n\n"
    
    # Process each page
    try:
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        md_content += f"## Summary\n\nThis document contains {total_pages} pages.\n\n"
        
        for page_num, page in enumerate(doc):
            md_content += f"## Page {page_num + 1}\n\n"
            
            # Extract text
            text = page.get_text()
            if text.strip():
                md_content += f"{text}\n\n"
            
            # Extract images
            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                
                # Save image to file
                img_filename = f"{sanitized_name}_page{page_num+1}_img{img_index+1}.png"
                img_path = os.path.join(img_dir, img_filename)
                
                with open(img_path, "wb") as img_file:
                    img_file.write(image_bytes)
                
                # Add image reference to markdown
                md_content += f"![Image from page {page_num+1}](img/{img_filename})\n\n"
        
        # Save markdown file
        md_file_path = os.path.join(md_dir, f"{sanitized_name}.md")
        with open(md_file_path, "w", encoding="utf-8") as md_file:
            md_file.write(md_content)
        
        return md_file_path
    
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return None

def update_mkdocs_config(md_file_path, mkdocs_yml_path="mkdocs.yml"):
    """
    Add the generated markdown file to the mkdocs.yml navigation.
    This is a simple implementation - in practice you might want more control.
    """
    try:
        import yaml
        
        # Read existing config
        with open(mkdocs_yml_path, 'r') as f:
            config = yaml.safe_load(f)
        
        # Get relative path for markdown file
        docs_dir = config.get('docs_dir', 'docs')
        rel_path = os.path.relpath(md_file_path, docs_dir)
        
        # Create a simple title from the filename
        title = os.path.splitext(os.path.basename(md_file_path))[0].replace('_', ' ').title()
        
        # Check if PDF section exists
        nav = config.get('nav', [])
        pdf_section = None
        
        for item in nav:
            if isinstance(item, dict) and 'PDF Documents' in item:
                pdf_section = item['PDF Documents']
                break
        
        # If no PDF section exists, create one
        if pdf_section is None:
            nav.append({'PDF Documents': [{'PDF Extract': rel_path}]})
        else:
            if isinstance(pdf_section, list):
                pdf_section.append({title: rel_path})
            else:
                item['PDF Documents'] = [pdf_section, {title: rel_path}]
        
        # Write updated config
        with open(mkdocs_yml_path, 'w') as f:
            yaml.dump(config, f, default_flow_style=False)
        
        print(f"Updated {mkdocs_yml_path} with new PDF extract")
    
    except Exception as e:
        print(f"Error updating mkdocs.yml: {e}")
        print("You'll need to manually add the markdown file to your navigation.")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Convert PDF to Markdown for MkDocs")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--output-dir", "-o", default=DEFAULT_OUTPUT_DIR, 
                        help=f"Output directory (default: {DEFAULT_OUTPUT_DIR})")
    parser.add_argument("--update-config", "-u", action="store_true",
                        help="Update mkdocs.yml with the new markdown file")
    
    args = parser.parse_args()
    
    # Process PDF
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Processing {args.pdf_path}...")
    md_file_path = extract_pdf_content(args.pdf_path, args.output_dir)
    
    if md_file_path:
        print(f"Successfully converted PDF to: {md_file_path}")
        
        if args.update_config:
            update_mkdocs_config(md_file_path)
    else:
        print("PDF conversion failed.")

if __name__ == "__main__":
    main()