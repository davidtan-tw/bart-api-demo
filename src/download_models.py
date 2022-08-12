from transformers import pipeline

print("Downloading model...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
print("Done.")
