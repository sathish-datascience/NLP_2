import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

mylist = stopwords.words("english")

text = "hello everyone datascience is very good subject all company's are using this sofware"

output = [word for word in text.split() if word not in mylist]

print(output)

import nltk
from textblob import TextBlob
nltk.download("averaged_preseptron_tagger")


text = "hello everyone datascience is very good subject all company's are using this sofware"

output = TextBlob(text)

print(output.tags)
