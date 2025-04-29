def summarize_text(text):
    return text[:100] + "..." if len(text) > 100 else text