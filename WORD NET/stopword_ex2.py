import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

mylist  = stopwords.words("english")

ab_word = ["idiot","stupid","bad" ,"abuse notgood waste fail stupid broot"]

t_list = mylist + ab_word

text = "yesterday i watch the  movie rrr that was so good music was average when the intervel popcorn was bad i  idiot with stupid cannt tast it"

postpa = [word for word in text.split() if word not in t_list]

print(postpa)

