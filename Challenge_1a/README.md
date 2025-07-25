# 🧠 Challenge 1a: PDF Processing Solution

## 🚀 Overview
This is our submission for **Challenge 1a** of the **Adobe India Hackathon 2025** — where we transform raw PDFs into structured JSON outlines using a Dockerized solution.

## 📦 What It Does
- Automatically processes all PDFs from `/app/input`
- Outputs structured outlines in JSON format to `/app/output`
- Runs inside a lightweight Docker container (≤ 200MB, no internet, CPU-only)

## 🛠️ Tech Stack
- Python 3.10
- PyMuPDF (for PDF parsing)
- Docker (CPU-only container, linux/amd64)

## 📁 Project Structure
Challenge_1a/
├── sample_dataset/
│ ├── pdfs/ # Input PDFs
│ ├── outputs/ # Expected JSON outputs
│ └── schema/ # Output JSON schema
├── process_pdfs.py # Main processing script
├── Dockerfile # Container setup
└── README.md # You're here!

### 🧱 Build Docker Image
```bash
docker build --platform linux/amd64 -t pdf-processor .
```

### 🚀 Run the Processor
```bash
docker run --rm \
  -v $(pwd)/sample_dataset/pdfs:/app/input:ro \
  -v $(pwd)/sample_dataset/outputs:/app/output \
  --network none \
  pdf-processor
```

## 📤 Output Format

- **Output**: One `.json` file per `.pdf` file
- **Schema**: Matches `sample_dataset/schema/output_schema.json`
- **Structure**:
  - `title`: Title of the document
  - `outline`: List of sections with:
    - `level` (e.g., H1, H2, H3)
    - `text` (section heading)
    - `page` (page number)

---

## 🧪 Constraints Checklist

- ✅ Processes all PDFs from `/app/input`
- ✅ Generates valid `.json` output per file
- ✅ Completes within **10 seconds** for 50-page PDFs
- ✅ Runs fully **offline** (no network access)
- ✅ CPU-only (no GPU)
- ✅ Output follows the provided schema strictly
- ✅ Docker image size is **under 200MB**
- ✅ Built for `linux/amd64` (no `arm64` support)
