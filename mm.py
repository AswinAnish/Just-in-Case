import numpy as np
r=int(input("Enter the no.of rows"))
c=int(input("Enter the no.of columns"))
a=[]
b=[]
print("ENTER THE ELEMENTS ROW WISE")
print("ENTER THE ELEMENTS OF MATRIX")
for i in range(r):
 for j in range(c):
  e=int(input("element"))
  a.append(e)
a=np.array(a).reshape(r,c)
print("ENTER THE ELEMENT OF MATRIX 2")
for i in range(r):
 for j in range(c):
  e=int(input("element"))
  b.append(e)
b=np.array(b).reshape(r,c)
c=np.add(a,b)
print("matrix1",a)
print("matrix2",b)
print("resultant matrix",c)
c_t=c.transpose()

