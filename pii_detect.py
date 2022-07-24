import pandas as pd
import docx
import torch
from sentence_transformers import SentenceTransformer, util
import nltk
import docx
from keybert import KeyBERT
nltk.download('stopwords')
embedder = SentenceTransformer('all-MiniLM-L6-v2')  
bert = KeyBERT()

embedder = SentenceTransformer('all-MiniLM-L6-v2')

df = pd.read_csv('C:/Users/adity/Downloads/Tags2.csv',
                 sep=',', engine='python')#enter the path of the tags file manually
#print(df)

dict_risk_cats_ = {}
for i in range(len(df)):

    key = df['Tags'][i]
    vals = (df['Keywords'][i].split(','))

    dict_risk_cats_[key] = vals
print(dict_risk_cats_)


# defining a function which checks the cosine similarity between the legend:keywords and the
def cosine_sim_check(actual_word):
    #corpus of words generated.
    actual_word = actual_word
    actual_word_emb = embedder.encode(actual_word, convert_to_tensor=True)
    scor = []
    max_scor = []  # to compute the max_score of cosine similarity
    for e in dict_risk_cats_.values():

        dict_word_emb = embedder.encode(e, convert_to_tensor=True)
        scor.append([each.item() for each in util.cos_sim(
            actual_word_emb, dict_word_emb)[0]])
        max_scor.append([max(each) for each in scor])

    final_max_scor = max(max_scor[-1])
    final_max_index = max_scor[-1].index(max(max_scor[-1]))
    return list(dict_risk_cats_.keys())[final_max_index]

def query_parser(query):
    x = query
    x = x.replace('AND', '}').replace('}', '{')
    x = x.split('{')
    x = [each.strip() for each in x if each.strip() != '']
    x = [each.split('OR') for each in x]
    return x
# building the keybert keyword extractor model which extracts keywords from the
def keybert_extractor(text, gram1, gram2, top_res):
    #corpus file in a specific n_gram_range.
    keywords = bert.extract_keywords(text, keyphrase_ngram_range=(
        gram1, gram2), stop_words="english", top_n=top_res)
    results = []
    for scored_keywords in keywords:
        for keyword in scored_keywords:
            if isinstance(keyword, str):
                results.append(keyword)
    return results


# a method to generate the corpus of the doc given as input to our match_query(test category)
def corpus_generator(text0):
    #to it's specific keyword.
    corpus = keybert_extractor(text0, 3, 5, 10000)
    #of 3 and 5 gives it as input to the match_query function.
    return corpus


def match_query_21(text0, query_all):#this function is the main one and is called such that all the other functions are called

    corpus = corpus_generator(text0)
    query = query_parser(query_all)
    lst_ = []
    category_individual = []

    corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)

    # top_k = min(5, len(corpus))
    max_score_lst = []
    final_flatten_query_lst = []
    for terms in query:

        for each_term in terms:
            score_ = []
            query_embedding = embedder.encode(
                each_term, convert_to_tensor=True)
            cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]

            top_results = torch.topk(cos_scores, k=3)
            for score, idx in zip(top_results[0], top_results[1]):
                score_.append(score)
            max_score = max(score_)
            final_flatten_query_lst.append(each_term)
            max_score_lst.append(max_score)


    lth = [len(each) for each in query]
    # print(lth)

    score_lst = []
    highest_cat = []
    each_max_score = []
    count = 0
    for each_len in lth:
        each_score = max(max_score_lst[count:each_len+count])
        score_lst.append(each_score)

        index_each_score = max_score_lst.index(each_score)
        highest_cat.append(final_flatten_query_lst[index_each_score])
        each_max_score.append(each_score)
        count = each_len + count

    for each_highest in highest_cat:
        category_individual.append(cosine_sim_check(each_highest))

    cosine_sim = sum(score_lst)/len(lth)


#     print(category_individual)

    if cosine_sim.item() <= 0.35:
        risk = 'Low'
    elif cosine_sim.item() > 0.35 and cosine_sim.item() <= 0.6:
        risk = 'Medium'
    elif cosine_sim.item() > 0.6 and cosine_sim.item() <= 0.9:
        risk = 'High'
    else:
        risk = 'Very High'

    print('\n')
    print("The Content of PII/Sensitive Data is:", risk)#the variable risk contains our tag to be given to our data so return risk
    print("The cosine_sim of the item is:",cosine_sim.item())#this score and print just for reference
    return cosine_sim.item(), risk
    

query_all1 = "credit card AND bank account AND social security AND license AND email AND aadhar AND uid AND pan AND government of India AND passsport AND income tax AND property papers AND debit card AND transaction AND insurance AND ifsc AND SSN AND address AND law AND legal AND minority AND caste AND reserved category AND postal address AND medical records AND identification AND date of birth AND ip address AND health AND authority AND organization AND data protection AND admission"

#call match_query_21 and dont remove query_all1



