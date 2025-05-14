import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")

mylist = stopwords.words("english")

text = "hello this is sathish am from hyderabad"

output  = [word for word in text.split() if word not in mylist]

print(text)
print()
print(output)


