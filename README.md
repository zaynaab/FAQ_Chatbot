# NLP-Based FAQ Chatbot Using TF-IDF and Cosine Similarity

## Overview

This project is an NLP-based FAQ chatbot developed for an e-commerce/online shopping scenario.

The chatbot processes user questions and finds the most relevant FAQ using TF-IDF vectorization and cosine similarity. It then returns the corresponding answer.

The project uses traditional NLP techniques and does not require an external API or LLM.

## Features

- FAQ dataset stored in CSV format
- Text preprocessing using NLTK
- TF-IDF feature extraction
- Cosine similarity for FAQ matching
- Similarity threshold for irrelevant questions
- Interactive terminal chatbot
- Streamlit web-based chat interface

## Technologies Used

- Python
- NLTK
- Pandas
- Scikit-learn
- Streamlit

## Project Architecture

User Question  
↓  
Text Preprocessing  
↓  
TF-IDF Vectorization  
↓  
Cosine Similarity  
↓  
Best FAQ Match  
↓  
Similarity Threshold  
↓  
Chatbot Response

## Project Structure

```text
FAQ_Chatbot/
│
├── app.py
├── test_chatbot.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── faqs.csv
│
└── src/
    ├── __init__.py
    ├── preprocessing.py
    └── chatbot.py