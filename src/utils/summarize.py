from summarizer.sbert import SBertSummarizer


# source : https://pypi.org/project/bert-extractive-summarizer/#use-sbert (id doesn't seem to work, so go to SBert chapter)
def summarize(text, num_sentences=2):
    # initialize SBertSummarizer model (was loaded in build.py)
    model = SBertSummarizer("paraphrase-MiniLM-L6-v2")

    # generate summary of the text with only 2 sentences
    return model(text, num_sentences=num_sentences)
