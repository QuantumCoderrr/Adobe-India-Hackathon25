import json
from pathlib import Path
import fitz  # PyMuPDF

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    font_sizes = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        size = span["size"]
                        if text and len(text.split()) < 15:  # Filter out large paragraphs
                            font_sizes.append(size)
                            outline.append({
                                "text": text,
                                "page": page_num,
                                "font_size": size
                            })

    if not outline:
        return {"title": "Untitled", "outline": []}

    # Determine heading levels from font sizes
    sorted_fonts = sorted(set(font_sizes), reverse=True)
    font_to_level = {}
    for i, size in enumerate(sorted_fonts):
        level = f"H{i+1}" if i < 3 else "H3"
        font_to_level[size] = level

    structured_outline = []
    for item in outline:
        level = font_to_level.get(item["font_size"], "H3")
        structured_outline.append({
            "level": level,
            "text": item["text"],
            "page": item["page"]
        })

    return {
        "title": structured_outline[0]["text"] if structured_outline else "Untitled",
        "outline": structured_outline
    }

def process_pdfs():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_files = list(input_dir.glob("*.pdf"))

    if not pdf_files:
        print("⚠️ No PDF files found in /app/input")
        return

    for pdf_file in pdf_files:
        try:
            result = extract_outline(pdf_file)
            output_file = output_dir / f"{pdf_file.stem}.json"
            with open(output_file, "w") as f:
                json.dump(result, f, indent=2)
            print(f"✅ Processed: {pdf_file.name} ➜ {output_file.name}")
        except Exception as e:
            print(f"❌ Failed to process {pdf_file.name}: {str(e)}")

if __name__ == "__main__":
    print("🚀 Starting PDF outline extraction...")
    process_pdfs()
    print("🏁 All PDFs processed.")
