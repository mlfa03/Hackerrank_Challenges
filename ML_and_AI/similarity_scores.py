# Similarity Scores

import collections
import math

doc_words_count = collections.defaultdict(lambda: 0.0)
doc_count_containing_words = collections.defaultdict(lambda: 0.0)
total_doc = 4.0
tfidf = [[], [], [], []]

train = ["I'd like an apple.", "An apple a day keeps the doctor away.",
         "Never compare an apple to an orange.", "I prefer scikit-learn to orange."]

words = []
for i in range(len(train)):
    for word in train[i].split():
        word = word.lower().strip('.')        #removing the dot in the sentences 
        doc_words_count[word + str(i)] += 1

for text in train:
    text = text.strip('.')
    for word in text.split():                #this splits each sentence in train list into a list of words
        if word not in words:
            words.append(word.lower())       #list of words from the train list, each word is an element in the list

#Running the counter
#Words is a list of unique words in the train
for word in words:
    for text in train:
        text = text.lower()                        #everything in lowercase
        if word in text:
            doc_count_containing_words[word] += 1. #dictionary with count of words

sample = train[0].strip('.').split()

for word in words:
    word = word.lower()
    for i in range(len(train)):
        tfidf[i].append(doc_words_count[word+str(i)] *
                        math.log(total_doc/(doc_count_containing_words[word])))


def dotsum(a, b):
    return sum([i*j for (i, j) in zip(a, b)])


maxsimilarity = 0
for i in range(1, len(train)):
    similarity = dotsum(tfidf[0], tfidf[i])
    if similarity > maxsimilarity:
        maxsimilarity = i

print(maxsimilarity + 1)
