# 🚀 Adobe India Hackathon 2025 – "Connecting the Dots"

## 🔍 Rethink Reading. Rediscover Knowledge.

Imagine a world where PDFs aren’t just passive documents — but intelligent, interactive companions that **understand structure**, **connect ideas**, and **respond meaningfully**. That’s the mission of Adobe’s *Connecting the Dots* challenge — and this repository is our response to it.

---

## 📌 Problem Statement

In an era where we’re flooded with digital documents, the real power lies not in reading more — but in reading smarter. Adobe’s challenge asked us to:
- ✅ Extract intelligent outlines from PDFs (**Challenge 1A**)
- ✅ Identify section-specific content based on user personas (**Challenge 1B**)
- 🧠 Do it all with lightweight models, on-device, and with high accuracy
- 📦 Wrap everything in reproducible, portable Docker containers

---

## 🧠 Solutions Overview

### 🔹 Challenge 1A – Structured PDF Outline Extraction

**Objective**: Build a Python script that processes a directory of PDFs and returns JSON-formatted outlines — capturing headings, structure, and page numbers.

- 🛠 Built with `PyMuPDF` (fitz) for PDF parsing
- 📂 Input/output via CLI arguments
- 🐳 Packaged in a Docker container for seamless execution
- 📄 Outputs: Individual `.json` files per PDF with structural metadata

📁 Folder: [`Challenge_1a`](./Challenge_1a)

➡️ Includes:
- `process_pdfs.py`
- `Dockerfile`
- `sample_dataset/` (PDFs)
- `output/` (Generated JSON files)

---

### 🔹 Challenge 1B – Persona-Driven Section Extraction

**Objective**: For a given set of PDFs and a `challenge1b_input.json`, extract and rank the top 5 most relevant sections based on a specified user persona.

- 🤖 Used `sentence-transformers (MiniLM)` for semantic embeddings
- 📊 Applied `cosine similarity` (via scikit-learn) for ranking sections
- 🧾 Output format aligned with provided sample files
- 🐳 Docker-ready, CPU-efficient, <1GB

📁 Folder: [`Challenge_1b`](./Challenge_1b)

➡️ Includes:
- `process_documents.py`
- `Dockerfile`
- Collections 1–3 with:
  - PDFs
  - Input prompts
  - Output JSONs (predicted sections)

---

## 🐳 Docker Instructions (For Judges)

Each challenge can be run independently in Docker.

### 🏗 Build Image

```bash
docker build --platform linux/amd64 -t adobe_round1a ./Challenge_1a
docker build --platform linux/amd64 -t adobe_round1b ./Challenge_1b
```

### ▶️ Run Container
```bash
docker run --rm \
  -v $(pwd)/Challenge_1a/input:/app/input \
  -v $(pwd)/Challenge_1a/output:/app/output \
  --network none \
  adobe_round1a
```
```bash
docker run --rm \
  -v $(pwd)/Challenge_1b/input:/app/input \
  -v $(pwd)/Challenge_1b/output:/app/output \
  --network none \
  adobe_round1b
```

## 🧑‍💻 Team

- **Sandip Ghosh** — [GitHub: @QuantumCoderrr](https://github.com/QuantumCoderrr)  
- **Sandhita Poddar** — [GitHub: @CelestialCoderrr](https://github.com/CelestialCoderrr)  

Together, we built something that doesn't just read PDFs — it *understands* them.
