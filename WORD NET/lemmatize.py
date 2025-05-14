import nltk
from nltk.stem import WordNetLemmatizer

wl = WordNetLemmatizer()

text = 'winner win winning winner won'

tokens = text.split()

for word in tokens:
	print("Lemmatization for {} is {} ".format(word,wl.lemmatize(word)))


