import nltk

from textblob import TextBlob

nltk.download('averaged_perceptron_taggers')

text = "good morning this is satish from hyd"

output = TextBlob(text)

print(output.tags)

