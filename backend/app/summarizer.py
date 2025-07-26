from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def get_summary(text: str) -> str:
    chunks = [text[i:i+1024] for i in range(0, len(text), 1024)]
    summaries = [summarizer(chunk)[0]['summary_text'] for chunk in chunks]
    return " ".join(summaries)
