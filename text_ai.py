from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(text: str):
    summary = summarizer(text, max_length=100, min_length=25, do_sample=False)
    return summary[0]['summary_text']
