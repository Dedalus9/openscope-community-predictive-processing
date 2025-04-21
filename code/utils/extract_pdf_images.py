#!/usr/bin/env python3
"""
extract_pdf_images.py - Extract images from PDF files
"""

import os
import fitz  # PyMuPDF
import argparse
from PIL import Image
import io

def extract_images(pdf_path, output_dir=None, min_size=100):
    """
    Extract images from a PDF file and save them as PNG files.
    
    Args:
        pdf_path (str): Path to the PDF file
        output_dir (str): Directory to save the extracted images
        min_size (int): Minimum size (width or height) for images to extract
    
    Returns:
        list: Paths to the extracted image files
    """
    pdf_filename = os.path.basename(pdf_path)
    pdf_name = os.path.splitext(pdf_filename)[0]
    
    # Create output directory if not specified
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(pdf_path), f"{pdf_name}_images")
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    extracted_files = []
    
    # Counter for naming images
    image_count = 0
    
    print(f"Processing PDF: {pdf_path}")
    print(f"Extracting images to: {output_dir}")
    print(f"PDF has {len(pdf_document)} pages")
    
    # Iterate through pages
    for page_num, page in enumerate(pdf_document):
        # Get images from the page
        image_list = page.get_images(full=True)
        
        if not image_list:
            continue
            
        print(f"Found {len(image_list)} images on page {page_num + 1}")
        
        # Extract and save each image
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            
            # Open image with PIL to check size and convert format
            image = Image.open(io.BytesIO(image_bytes))
            
            # Skip small images (likely icons, bullets, etc.)
            if image.width < min_size and image.height < min_size:
                print(f"  Skipping small image: {image.width}x{image.height}")
                continue
                
            image_count += 1
            # Create a descriptive filename including page number and image dimensions
            image_filename = f"{pdf_name}_page{page_num+1:03d}_img{image_count:03d}_{image.width}x{image.height}.png"
            image_path = os.path.join(output_dir, image_filename)
            
            # Save as PNG for better quality
            image.save(image_path, "PNG")
            extracted_files.append(image_path)
            
            print(f"  Saved: {image_filename} ({image.width}x{image.height})")
    
    print(f"Extracted {len(extracted_files)} images total")
    return extracted_files

def extract_pages_as_images(pdf_path, output_dir=None, resolution=300, pages=None):
    """
    Extract entire pages from a PDF file as PNG images.
    
    Args:
        pdf_path (str): Path to the PDF file
        output_dir (str): Directory to save the extracted pages
        resolution (int): DPI resolution for rendering
        pages (list): List of page numbers to extract (1-based indexing)
    
    Returns:
        list: Paths to the extracted page images
    """
    pdf_filename = os.path.basename(pdf_path)
    pdf_name = os.path.splitext(pdf_filename)[0]
    
    # Create output directory if not specified
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(pdf_path), f"{pdf_name}_pages")
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    extracted_files = []
    
    # Calculate zoom factor based on resolution (PyMuPDF uses 72 dpi as base)
    zoom = resolution / 72
    
    # Define page range to process
    if pages:
        # Convert from 1-based to 0-based indexing
        pages_to_process = [p-1 for p in pages if 0 < p <= len(pdf_document)]
    else:
        pages_to_process = range(len(pdf_document))
    
    print(f"Processing PDF: {pdf_path}")
    print(f"Extracting pages to: {output_dir}")
    print(f"PDF has {len(pdf_document)} pages, extracting pages {[p+1 for p in pages_to_process]}")
    
    # Iterate through selected pages
    for page_num in pages_to_process:
        page = pdf_document.load_page(page_num)
        
        # Create matrix for high-resolution rendering
        matrix = fitz.Matrix(zoom, zoom)
        
        # Render page to pixmap (image)
        pixmap = page.get_pixmap(matrix=matrix, alpha=False)
        
        # Create a descriptive filename including page number
        image_filename = f"{pdf_name}_page{page_num+1:03d}.png"
        image_path = os.path.join(output_dir, image_filename)
        
        # Save as PNG
        pixmap.save(image_path)
        extracted_files.append(image_path)
        
        print(f"  Saved: {image_filename} ({pixmap.width}x{pixmap.height})")
    
    print(f"Extracted {len(extracted_files)} pages total")
    return extracted_files

def main():
    parser = argparse.ArgumentParser(description="Extract images and pages from PDF files")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--output", "-o", help="Output directory for extracted images/pages")
    parser.add_argument("--min-size", type=int, default=100, 
                        help="Minimum size (width or height) for images to extract (default: 100px)")
    parser.add_argument("--resolution", "-r", type=int, default=300,
                        help="Resolution in DPI for page rendering (default: 300)")
    parser.add_argument("--pages", "-p", type=int, nargs="+",
                        help="Page numbers to extract as images (1-based indexing)")
    parser.add_argument("--extract-mode", "-m", choices=["images", "pages", "both"], default="images",
                        help="What to extract: embedded images, full pages as images, or both (default: images)")
    
    args = parser.parse_args()
    
    if args.extract_mode in ["images", "both"]:
        extract_images(args.pdf_path, args.output, args.min_size)
    
    if args.extract_mode in ["pages", "both"]:
        extract_pages_as_images(args.pdf_path, args.output, args.resolution, args.pages)

if __name__ == "__main__":
    main()