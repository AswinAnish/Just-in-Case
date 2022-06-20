n = int(input("Enter the length of the list "))
l=[]
l2=[]
l3=[]
print("Enter the elements for the list ")
for i in range(0, n):
	ele=int(input())
	l.append(ele)
print(l)

n2 = int(input("Enter the length of the list "))
l2=[]
print("Enter the elements for the list ")
for i in range(0, n2):
	ele=int(input())
	l2.append(ele)
print(l2)
product = 1
for x in l:
	for r in l2:
		product=x*r
		l3.append(product)
cd 0.		product = 1
print(l3)
cd
