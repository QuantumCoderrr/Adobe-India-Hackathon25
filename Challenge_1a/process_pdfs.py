import fitz  # PyMuPDF
from pathlib import Path
import json
from collections import defaultdict

def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    font_count = defaultdict(int)
    spans_data = []

    # First pass: collect font sizes
    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    text = span["text"].strip()
                    if len(text) > 3:
                        font_size = round(span["size"], 1)
                        font_count[font_size] += 1
                        spans_data.append({
                            "text": text,
                            "size": font_size,
                            "page": page_num + 1,
                            "font": span.get("font", "")
                        })

    # Detect top 3 most used font sizes
    sorted_fonts = sorted(font_count.items(), key=lambda x: -x[0])  # sort by size descending
    heading_map = {}
    for i, (font_size, _) in enumerate(sorted_fonts[:3]):
        level = f"H{i+1}"
        heading_map[font_size] = level

    headings = []
    seen = set()
    for span in spans_data:
        size = span["size"]
        if size in heading_map and span["text"] not in seen:
            headings.append({
                "level": heading_map[size],
                "text": span["text"],
                "page": span["page"]
            })
            seen.add(span["text"])

    return headings

def process_all():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")

    for pdf_file in input_dir.glob("*.pdf"):
        title = pdf_file.stem
        headings = extract_headings(str(pdf_file))
        output = {
            "title": title,
            "outline": headings
        }
        with open(output_dir / f"{pdf_file.stem}.json", "w") as f:
            json.dump(output, f, indent=2)

if __name__ == "__main__":
    process_all()
