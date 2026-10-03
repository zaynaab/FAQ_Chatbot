import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")


def preprocess_text(text):
    """
    Clean and preprocess text using NLTK.
    """

    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation and special characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Tokenize text
    tokens = word_tokenize(text)

    # Get English stopwords
    stop_words = set(stopwords.words("english"))

    # Remove stopwords
    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    # Join tokens back into a string
    cleaned_text = " ".join(tokens)

    return cleaned_text