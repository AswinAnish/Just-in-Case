import re
password = input("Enter the Password ")
flag=0
while(True):
	if not len(password)<6:
		flag=1
		break
	elif not re.search([A-Z], password):
		flag=1
		break
	elif not re.search([a-z], password):
		flag=1
		break
	elif not re.search([0-9], password):
		flag=1
		break
	elif not re.search(['@','#','$'], password):
		flag=1
		break
	else:
		flag=0
if flag==0:
	print("Password is valid ")
else:
	print("Password is not valid ")
