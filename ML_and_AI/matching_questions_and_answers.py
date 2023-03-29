# Matching questions and their answers 
# 2 test cases failed, others passed 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

from numpy import argmax
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline
from sklearn.metrics.pairwise import cosine_similarity


# parse the paragraph, split into sentences
par_splitter = re.compile(r'[\.?!] ?| - ')
paragraph = [sent for sent in par_splitter.split(input()) if sent is not '']

# learn tfidf vectors and LSI space from paragraph
# Latent Semantic Indexing (LSI) is commonly used to match queries to documents in information #retrieval appli- cations
lsi_pipe = Pipeline([
        ('tfidf', TfidfVectorizer(max_df=0.8, ngram_range=(2,4))),
        ('lsi', TruncatedSVD(n_components=200))
    ])
lsi_pipe.fit(paragraph)

# parse the questions and answers
questions = []
for i in range(5):
    questions.append(input())
answers = input().split(';')

# transform questions and answers into LSI space
questions_lsi = lsi_pipe.transform(questions)
answers_lsi = lsi_pipe.transform(answers)

# compute pairwise cosine similarity between questions and answers
sims = cosine_similarity(questions_lsi, answers_lsi)

# print the most similar answer for each question
for i in range(5):
    print(answers[argmax(sims[i])])

# TF_IDF : max_df float or int, default=1.0
# When building the vocabulary ignore terms that have a document frequency strictly higher than the given threshold (corpus-specific stop words). 
# If float in range [0.0, 1.0], the parameter represents a proportion of documents, integer absolute counts. 
# This parameter is ignored if vocabulary is not None.
