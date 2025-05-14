import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")

mylist = stopwords.words("english")

text = "hi hello this is satish from ramanthapur how are you all"

output = [word for word in text.split() if word not in mylist]

print(output)
print()

import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")

mylist = stopwords.words("english")

text = "we are from naresh it my name is sathish am form ramanthapur doing training now hope we getting job like datascientist"

output1 = [word for word in text.split() if word not in mylist]

print(output1)

