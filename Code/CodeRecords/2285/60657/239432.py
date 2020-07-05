import math
import re
num=input()
am1=input()
num1=input().split(' ')
num1=[int(x) for x in num1]
am2=input()
num2=input().split(' ')
num2=[int(x) for x in num2]
cons=[]
con=[]
days=0
mark=0
i=0
for i in range(0,len(num1)-1):
    if(num1[i+1]<num1[i]):
        cons.append(i)
i=0
lista=[]
for k in range(0,len(num1)):
    lista.append(k)
for k in range(0,len(cons)):
    if(cons[0]!=0):
        con.append((0,0+cons[i]))
        con.append((cons[i]+1,len(num1)-1))
    else:
        con.append((1,cons[i]))
        con.append((cons[i]+1,len(num1)-1))

cons1=[]
con1=[]

for i in range(0,len(num2)-1):
    if(num2[i+1]<num2[i]):
        cons1.append(i)
i=0
listb=[]
for k in range(0,len(num2)):
    listb.append(k)
for k in range(0,len(cons1)):
    if(cons1[0]!=0):
        con1.append((0,0+cons1[i]))
        con1.append((cons1[i]+1,len(num2)-1))
    else:
        con1.append((1,cons1[1]))
        con1.append((cons1[1]+1,len(num2)-1))


print("("+str(con[0][0]),str(con[0][1])+")","("+str(con[1][0]),str(con[1][1])+")")
print("("+str(con1[0][0]),str(con1[0][1])+")","("+str(con1[1][0]),str(con1[1][1])+")")



