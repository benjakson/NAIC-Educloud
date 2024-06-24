import sys
from docx import Document
from transformers import pipeline

def main():
    if len(sys.argv) > 1:  # More than one argument means user provided input
        filename = sys.argv[1]  # Take the first argument after the script name
        process_input(filename)
    else:
        #filename = input("Please enter your input: ")  # Prompt user for input
        print("Pleae provide the full path to the document")

def remove_extra_spaces(text):
    # Split on whitespace, then rejoin with single spaces
    return ' '.join(text.split())

def process_input(filename):
    # Placeholder for processing the input
    print(f"Processing input: {filename}")

    # Load the .docx file
    doc = Document(filename)
    document= []
    #cnt = 0
    for para in doc.paragraphs:
        if para.text.strip(): 
          cleaned_text = remove_extra_spaces(para.text).replace('\r', '======').replace('\n', '=======')
          document.append(cleaned_text)
    document = " ".join(document)
    print("First 60 characters of document:", document[:60])
    # start_summary(document)


def start_summary(document):
    #print(document)
    words = document.split()
    doc_length = len(words)
    print(doc_length)
    #model_name = "meta-llama/Meta-Llama-3-70B-Instruct"
    #model_name = "meta-llama/Meta-Llama-3-8B"
    #model_name = "facebook/bart-large-cnn"
    #model_name = "norallm/normistral-7b-warm-instruct"
    #model_name = "facebook/bart-large-cnn"
    model_name = "Danish-summarisation/DanSumT5-large"

    # # Load a pre-trained model for summarization
    # #summarizer = pipeline("summarization",  model="bart-large-cnn", tokenizer="bart-large-cnn", framework="pt")
    #summarizer = pipeline("summarization",  model=model_name, tokenizer=model_name, framework="pt", max_length=1024, truncation=True, device=0)
    summarizer = pipeline("summarization",  model=model_name, tokenizer=model_name, framework="pt", max_length=1024, truncation=True, device=0)
    #summarizer = pipeline("summarization",  model=model_name, tokenizer=model_name, framework="pt", truncation=True, device=0)
    print("--------------------------summary------------")
    #summary = summarizer(document, max_length=830, min_length=130)
    summary = summarizer(document,min_length=230)
    # # Print the summarized text
    print(summary[0]['summary_text'])

if __name__ == "__main__":
    main()







