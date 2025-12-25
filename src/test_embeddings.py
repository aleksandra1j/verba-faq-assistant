from data_loader import load_faqs
from embedder import Embedder

if __name__ == "__main__":
    questions, answers = load_faqs("data/faq.json")

    embedder = Embedder()
    embeddings = embedder.encode(questions)

    print(f"Number of questions: {len(questions)}")
    print(f"Embedding shape: {embeddings.shape}")