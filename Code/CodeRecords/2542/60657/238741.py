import math
num2=input()
num2=num2[1:-1]
num2=num2.split(',')
num2=[int(x) for x in num2]
num2.sort()
cons=1
con=[]
for i in range(len(num2)-1):
    if num2[i+1]-num2[i]==1:
        cons+=1
    else:
        con.append(cons)
        cons=1
con.sort()
print(con[-1])