import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


data = {
    'Subject': ['Math', 'Math', 'Math','Math', 'Science', 'Science', 'Science', 'English', 'English'],
    'Score': [85, 90, 95, 99,78, 80, 88, 91, 93],
    'Gender': ['Male', 'Female','Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Female']
}

df = pd.DataFrame(data)


sns.barplot(data=df, x='Subject', y='Score',hue="Gender")


plt.show()
