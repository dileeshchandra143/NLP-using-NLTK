# sample stemming
# one more step of preprocessing the data
# considers stemwords of a sentence, replaces with normal words
# PorterStemmer is a stemming algorithm built into NLTK 

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
example = ["slow","slowly", "slowed", "slowing", "slowesting"]

for i in example:
    print(ps.stem(i))
