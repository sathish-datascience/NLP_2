import nltk

from textblob import TextBlob

nltk.download("averaged_perseptron_tagger")

text = "hey hello this is sathish from hyderabad"

output = TextBlob(text)

print(output.tags)