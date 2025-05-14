import nltk

from nltk.corpus import stopwords

nltk.download("stopwords")

mylist = stopwords.words("english")

text = "hi everyone this is satish from ramanthapur everyone is doing well have a nice day"


output = [word for word in text.split() if word not in mylist]

print(output)