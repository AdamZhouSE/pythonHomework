import sys
input=sys.stdin.readlines()
list=input[0]
a=list.replace('[','')
b=a.replace(']','')
c=b.replace('\n','')
d=c.split(',')
lower=int(input[1])
upper=int(input[2])
num=0
for x in range(0,len(d)):
    mod=int(d[x])
    if mod>=lower and mod<=upper:
        num=num+1
    for y in range(x+1,len(d)):
        mod=mod+int(d[y])
        if mod>=lower and mod<=upper:
            num=num+1
print(num,end='\n')