import nltk

from nltk.corpus import stopwords

nltk.download("stopwords")

mylist = stopwords.words('english')

text = "this is really good . how are you doing"

postpa = [word for word in text.split() if word not in mylist]

print(postpa)