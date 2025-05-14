plt.pie(gender ,
	labels = gender.index,
	autopct = "%1.1f%%",
	shadow = True,
	startangle = 90,
	explode = [0.03]*len(gender)
	)
plt.legend()
plt.show()
	