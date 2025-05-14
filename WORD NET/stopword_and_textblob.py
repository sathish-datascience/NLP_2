import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")

mylist = stopwords.words("english")

text = "hi hello this is satish from ramanthapur how are you all"

output = [word for word in text.split() if word not in mylist]

print(output)
print()

import nltk
from textblob import TextBlob
nltk.download("averaged_perceptron_tagger")

text_1 = "hi hello this is satish from ramanthapur how are you all sunday eating biriyani awesome"

output_1 = TextBlob(text_1)

print(output_1.tags)