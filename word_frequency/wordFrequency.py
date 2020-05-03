import numpy as np
from string import punctuation
import pandas as pd
import numpy as np
from collections import Counter
from nltk.corpus import stopwords

titles = pd.read_csv('papername.csv', index_col = False, header = None)
titles = list(np.array(titles).reshape(-1))
titleWords = []

# Change all the characters to lower character and get rid of punctuation
paperTitles = [i.lower() for i in titles]

for i in paperTitles:
    tmp = ''.join([c for c in i if c not in punctuation])
    titleWords.append(tmp)

# Split by and spaces, change the sentences into words
all_words = []
for i in titleWords:
    all_words.extend(i.split())

# Remove stopwords
en_stops = set(stopwords.words('english'))
words = []
for w in all_words:
    if w not in en_stops:
        words.append(w)

# Count the number of words, generate the feature vector
count = Counter(words)
vocab = sorted(count,key=count.get,reverse=True)
vocab = vocab[:50]

print(vocab)

