import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class Retriever:
    def __init__(self, questions, answers, embeddings):
        self.questions = questions
        self.answers = answers
        self.embeddings = embeddings

    def retrieve(self, query_embedding, top_k=3):    
        similarities = cosine_similarity(
            query_embedding.reshape(1, -1),
            self.embeddings
        )[0]

        top_indices = np.argsort(similarities)[::-1][:top_k]

        results = []
        for idx in top_indices:
            results.append({
                "question": self.questions[idx],
                "answer": self.answers[idx],
                "score": float(similarities[idx])
            })

        return results