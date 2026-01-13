from transformers import pipeline

# Load sentiment analysis pipeline
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def predict(text):
    result = classifier(text)[0]
    label = result["label"]
    score = result["score"]
    return label, score
