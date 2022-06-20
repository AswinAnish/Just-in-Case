import re
password = input("Enter the Password ")
if re.fullmatch(r'[A-Z, a-z, 0-9, @#$]{6,}', password):
	print("password is valid")
else:
	print("Password is not valid please try Again!!!!")
