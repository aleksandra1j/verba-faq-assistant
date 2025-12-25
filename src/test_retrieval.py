from data_loader import load_faqs
from embedder import Embedder
from retriever import Retriever

if __name__ == "__main__":
    questions, answers = load_faqs("data/faq.json")

    embedder = Embedder()
    faq_embeddings = embedder.encode(questions)

    retriever = Retriever(questions, answers, faq_embeddings)

    test_queries = [
        "I cannot log into my account",
        "How do I reset my password?",
        "I was charged twice on my credit card",
        "Не можам да се најавам на мојата сметка"
    ]

    for user_query in test_queries:
        query_embedding = embedder.encode([user_query])[0]
        results = retriever.retrieve(query_embedding, top_k=3)

        print("=" * 60)
        print(f"User query: {user_query}\n")

        for i, result in enumerate(results, start=1):
            print(f"Result {i}:")
            print(f"Question: {result['question']}")
            print(f"Answer: {result['answer']}")
            print(f"Similarity score: {result['score']:.4f}\n")