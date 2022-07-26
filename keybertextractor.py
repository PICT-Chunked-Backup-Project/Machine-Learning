from sklearn.feature_extraction.text import CountVectorizer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd


class keybertextracter:
    text=""

    def __init__(self,t):
        text=t

    def keywordextract(self):
        n_gram_range = (1, 1)
        stop_words = "english"
        count = CountVectorizer(ngram_range=n_gram_range,
                                stop_words=stop_words).fit([self.text])

        candidates = count.get_feature_names_out()

        model = SentenceTransformer('distilbert-base-nli-mean-tokens')
        doc_embedding = model.encode([self.text])
        candidate_embeddings = model.encode(candidates)

        top_n =5
        distances = cosine_similarity(doc_embedding, candidate_embeddings)
        keywords = [candidates[index] for index in distances.argsort()[0]][-top_n:]

        print(keywords)

        print(type(keywords))

        s = ",".join(keywords)

        print(s)
        return s
    # keywrdextract(data)
# if __name__ == "__main__":
#     c=keybertextracter(text)
#     c.keywordextract()
