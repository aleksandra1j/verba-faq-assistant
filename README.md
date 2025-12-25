# FAQ Retrieval Assistant

This project is a simple FAQ retrieval assistant designed to demonstrate how semantic similarity can be used to match user queries with relevant answers.

The system simulates a lightweight customer-support AI by retrieving the most relevant responses from a small FAQ knowledge base.

##  📌 Approach

1. **FAQ Dataset**
   - A small mock FAQ dataset (15 question–answer pairs) related to customer support topics such as:
     - Login & access
     - Password reset
     - Billing
     - Product information
     - Support contact
   - The dataset also includes examples in Macedonian to demonstrate multilingual support.

2. **Text Embeddings**
   - Each FAQ question is converted into a numerical vector (embedding) using a sentence embedding model.
   - *Embeddings capture the semantic meaning of the questions, not just keyword matching.*

3. **Query Processing**
   - A user query is embedded using the same model.
   - Cosine similarity is used to compare the query embedding with all FAQ embeddings.

4. **Retrieval**
   - The system retrieves the **top 3 most relevant FAQs** based on similarity scores.

5. **Best Answer & Confidence Logic**
   - The top-ranked FAQ (top-1) is selected as the best answer.
   - A confidence threshold is applied:
     - If similarity is high enough, the answer is returned.
     - If similarity is low, the system returns a safe fallback message instead of a potentially incorrect answer.


## 🛠 Tools Used

- **Python 3.12**
- **sentence-transformers**
  - Model: `all-MiniLM-L6-v2`
  - Used to generate semantic embeddings for questions and queries
- **NumPy**
  - Vector operations
- **scikit-learn**
  - Cosine similarity computation

## ▶️ How to Run the Project

   ```bash
   git clone https://github.com/aleksandra1j/verba-faq-assistant.git

   cd verba-faq-assistant
   python -m venv venv
   venv\Scripts\activate 

   pip install -r requirements.txt 

   python src/test_retrieval.py

```