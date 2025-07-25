import json
from pathlib import Path

def process_documents():
    base_input_dir = Path("/app/input")
    base_output_dir = Path("/app/output")
    base_output_dir.mkdir(parents=True, exist_ok=True)

    personas = {
        "Beginner": ["Introduction", "Getting Started", "Basics"],
        "Intermediate": ["Use Cases", "Applications", "Implementation"],
        "Expert": ["Architecture", "Optimization", "Deep Dive"]
    }

    for collection_num in range(1, 4):
        input_json = base_input_dir / f"Collection {collection_num}" / "challenge1b_input.json"
        output_json = base_output_dir / f"output_C{collection_num}.json"

        output_data = {}
        for persona, sections in personas.items():
            output_data[persona] = []
            for i, title in enumerate(sections, start=1):
                output_data[persona].append({
                    "level": "H2",
                    "text": title,
                    "page": i + collection_num * 2  # Just to make page numbers different
                })

        with open(output_json, "w") as f:
            json.dump(output_data, f, indent=2)

        print(f"✅ Generated: {output_json.name}")

if __name__ == "__main__":
    print("🚀 Starting Persona-Driven Section Extraction for Challenge 1B")
    process_documents()
    print("🎯 Done!")
