#import math as n
n = int(input("Enter the length of the list "))
l=[]
l2=[]
l3=[]
print("Enter the elements for the list ")
for i in range(0, n):
	ele=int(input())
	l.append(ele)
print(l)
product = 1
for x in l:
    product *= x
print("The result is ",product)
for x in l:
	for r in l2:
		product=x*r
		l3.append(product)
print(l3)
