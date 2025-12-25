import json
from pathlib import Path


def load_faqs(filepath: str):
    file_path = Path(filepath)

    with file_path.open(encoding="utf-8") as f:
        faqs = json.load(f)

    questions = [item["question"] for item in faqs]
    answers = [item["answer"] for item in faqs]

    return questions, answers
