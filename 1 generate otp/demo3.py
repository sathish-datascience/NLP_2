import random

def generate_otp():
	otp = "".join([str(random.randint(0,9)) for _ in range(6) ])

	return otp

otp = generate_otp()


print("Your 6 digit otp  is",otp)





def generate_ph():
	f = str(random.randint(6,9))
	otp = f+"".join([str(random.randint(0,9)) for _ in range(10) ])
	return otp

ph_no = generate_ph()

print("Your 10 digit Phone no is",ph_no)
