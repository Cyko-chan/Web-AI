import spacy
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the SpaCy model
nlp = spacy.load("en_core_web_md")

def summarize_text(text, num_sentences=2):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    
    # Create a similarity matrix
    sentence_vectors = np.array([doc[sent.start:sent.end].vector for sent in doc.sents])
    similarity_matrix = cosine_similarity(sentence_vectors)

    # Rank sentences based on their scores
    scores = similarity_matrix.sum(axis=1)
    ranked_sentences = [sentences[i] for i in np.argsort(scores, axis=0)[-num_sentences:]]

    return ' '.join(ranked_sentences)

# Example usage
if __name__ == "__main__":
    video_text = """
    Artificial Intelligence (AI) is a field of computer science that aims to create machines 
    capable of intelligent behavior. In recent years, AI has made significant strides in areas 
    such as natural language processing, computer vision, and robotics. As AI continues to evolve, 
    it is transforming industries and impacting our daily lives in profound ways.
    """

    summary = summarize_text(video_text)
    print("Original Text:\n", video_text)
    print("\nSummary:\n", summary)