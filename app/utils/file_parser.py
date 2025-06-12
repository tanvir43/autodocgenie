import os
from docx import Document


def parse_file(file_path: str) -> str:
    _, ext = os.path.splitext(file_path.lower())

    if ext == ".txt" or ext == ".md":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read().strip()

    elif ext == ".docx":
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])

    else:
        raise ValueError(f"Unsupported file type: {ext}")