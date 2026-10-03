import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.preprocessing import preprocess_text


class FAQChatbot:

    def __init__(self, faq_file):
        self.faqs = pd.read_csv(faq_file)

        self.faqs["processed_question"] = self.faqs["question"].apply(
            preprocess_text
        )

        self.vectorizer = TfidfVectorizer()

        self.faq_vectors = self.vectorizer.fit_transform(
            self.faqs["processed_question"]
        )

    def get_response(self, user_question):

        processed_question = preprocess_text(user_question)

        user_vector = self.vectorizer.transform([processed_question])

        similarities = cosine_similarity(
            user_vector,
            self.faq_vectors
        )

        best_match_index = similarities.argmax()

        best_score = similarities[0][best_match_index]

        threshold = 0.20

        if best_score >= threshold:
            answer = self.faqs.iloc[best_match_index]["answer"]
        else:
            answer = "Sorry, I couldn't find a relevant answer to your question."

        return answer, best_score