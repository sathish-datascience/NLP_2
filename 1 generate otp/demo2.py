import random

def generate_otp():

	otp = "".join([str(random.randint(0,9)) for _ in range(6)])
	return otp

otp = generate_otp()

print("Your 6 digit OTP is",otp)