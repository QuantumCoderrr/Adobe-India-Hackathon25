FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir PyMuPDF sentence-transformers scikit-learn

CMD ["python", "process_documents.py"]
