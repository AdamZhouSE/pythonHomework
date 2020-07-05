import math
a=list(eval(input()))
b=list(eval(input()))
c=list(eval(input()))
d=list(eval(input()))
n=len(a)
li=[]
li.append(a)
li.append(b)
li.append(c)
li.append(d)
count=0
for i in range(int(math.pow(n,4))):
    sum=0
    tmp=i
    j=0
    while(j!=4):
        sum+=li[j][tmp%n]
        tmp=tmp//n
        j+=1
    if sum==0:
        count+=1

print(count)
        