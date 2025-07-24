# Challenge 1A - Adobe Hackathon Submission

## 🔍 Problem
PDF Outline Extraction – heading detection and content structuring.

## 🧰 Tools Used
- Python
- PyMuPDF (`fitz`)
- spaCy (with Japanese model)
- Docker

## 📦 Folder Structure
- `input/` → place your PDFs here
- `output/` → JSONs will be auto-generated here
- `process_pdfs.py` → your processing logic
- `requirements.txt` → Python deps
- `Dockerfile` → for containerization

## 🐳 Run with Docker

```bash
docker build --platform linux/amd64 -t pdf-outliner .
docker run --rm \
  -v $(pwd)/input:/app/input:ro \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-outliner

## 💡 Notes

Handles multilingual PDFs (Japanese tested)
Works across multiple pages
No external API used

---


