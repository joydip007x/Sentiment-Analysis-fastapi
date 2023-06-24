from transformers import pipeline


# Using Twitter-roBERTa-base for Sentiment Analysis - UPDATED (2022) 
# URL:https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest 


sentiment_analyser = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    tokenizer="cardiffnlp/twitter-roberta-base-sentiment-latest"
)               

