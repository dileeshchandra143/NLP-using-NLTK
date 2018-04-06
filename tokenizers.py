# tokenizing is a form of grouping text
#two main components for tokenizing any body of text
#sentence tokenizer: groups by sentence
#Word tokenizer: groups by words

from nltk.tokenize import sent_tokenize, word_tokenize

example = ('Hello everyone, how are you? hope you are doing good. My window is opened and the air is cold!')

##print(sent_tokenize(example));
##print(word_tokenize(example));

for i in word_tokenize(example):
    print(i);
