import random

def generate_otp():
	first_digit = str(random.randint(6,9))
	otp = first_digit+"".join(  [str(random.randint(0,9)) for _ in range(10)]  )

	return otp


otp = generate_otp()

print("Your 6 digit OTP is",otp)