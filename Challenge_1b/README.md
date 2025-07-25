# 🧠 Challenge 1b: Multi-Collection PDF Analysis

## 📘 Overview
An advanced PDF content extraction solution tailored for **persona-driven** scenarios. It analyzes multiple PDF collections and extracts the most relevant content based on a given **persona** and their specific **job-to-be-done**.

## 📚 Collections Summary

### 🧳 Collection 1: Travel Planning
- **Challenge ID**: `round_1b_002`
- **Persona**: Travel Planner
- **Goal**: Plan a 4-day trip for 10 college friends to the South of France
- **Docs**: 7 regional travel guides

### 🧾 Collection 2: Adobe Acrobat Learning
- **Challenge ID**: `round_1b_003`
- **Persona**: HR Professional
- **Goal**: Design & manage fillable onboarding and compliance forms
- **Docs**: 15 Adobe Acrobat tutorials

### 🥗 Collection 3: Recipe Collection
- **Challenge ID**: `round_1b_001`
- **Persona**: Food Contractor
- **Goal**: Prepare a vegetarian buffet menu for a corporate dinner
- **Docs**: 9 vegetarian recipe PDFs

## 🔁 Input / Output Format

### 🔽 Input JSON
```json
{
  "challenge_info": {
    "challenge_id": "round_1b_XXX",
    "test_case_name": "specific_test_case"
  },
  "documents": [{"filename": "doc.pdf", "title": "Title"}],
  "persona": {"role": "User Persona"},
  "job_to_be_done": {"task": "Use case description"}
}
```

🔼 Output JSON
```json
{
  "metadata": {
    "input_documents": ["list of processed PDFs"],
    "persona": "User Persona",
    "job_to_be_done": "Task"
  },
  "extracted_sections": [
    {
      "document": "source.pdf",
      "section_title": "Extracted Section Heading",
      "importance_rank": 1,
      "page_number": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "source.pdf",
      "refined_text": "Summarized or directly relevant content",
      "page_number": 1
    }
  ]
}
```

## ✅ Key Features

- 🔍 **Persona-specific section extraction**  
  Extracts only the most relevant content tailored to the persona’s needs.

- 🏆 **Ranked content relevance (`importance_rank`)**  
  Assigns a rank to each section based on contextual importance.

- 📁 **Handles multi-PDF, multi-purpose collections**  
  Supports diverse document types and use cases across multiple collections.

- 🧾 **Schema-compliant structured output**  
  Ensures output adheres strictly to the required JSON format.
