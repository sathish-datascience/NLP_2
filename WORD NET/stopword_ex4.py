import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

mylist = stopwords.words('english')

text = "hi hello this is krishna. from ramnthapur.  i likes sweets very well."

output = text.split('.')

output1 = [word for word in text.split() if word not in mylist]

print(output)
print()
print(output1)
print()




import re

text = "data science0941 is very precisious the training peri1d o0f datascience is 6 months anyo0ne can lea4rn with good coach2"

out = re.sub(r'\d+','',text)

print(out)
print()

text2 = "good*&^ morning@#$%%^"

out_1 = re.sub(r'[^\w\s]','',text2)

print()
print(out_1)






