from src.chatbot import FAQChatbot


# Create chatbot
chatbot = FAQChatbot("data/faqs.csv")


# Test questions
test_questions = [
    "Where is my parcel?",
    "How long will delivery take?",
    "Can I return an item?",
    "How do I cancel my order?",
    "What payment methods do you accept?",
    "I forgot my password",
    "How do I apply a discount?",
    "What is the weather today?"
]


# Test each question
for question in test_questions:

    answer, score = chatbot.get_response(question)

    print("\nUser:", question)
    print("Bot:", answer)
    print("Similarity Score:", round(score, 2))