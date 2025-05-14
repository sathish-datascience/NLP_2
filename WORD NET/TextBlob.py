import nltk

from textblob import TextBlob

nltk.download("averaged_perceptron_tagger")


text = "hello how are you all good who is this"

output = TextBlob(text)

print(output)
print()
print(output.tags)
print()