# corpora and lexicon functionalities built into nltk used for preprocessing any body of text
#corpora can be used for for any kind of speech in english or some other languages, we can create our own tokenizers based on corpora
#Stop Words: the words which we need and computer dont need, like 'a', 'the', 'is' to filterout these words
#the words which are not necessary for data analysis can be filtered by

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


example = "This is an example to show the usage of stop words filtering"
stop_words = set(stopwords.words("english"))

words = word_tokenize(example)

filtered = []

for i in words:
    if i not in stop_words:
        filtered.append(i)

print(filtered)
