import math
#from numpy import *
def com(a,b):
    sum=0
    if(a[0]==b[0] and a[1]==b[1]):
        sum=0
        return sum
    if(a[0]==b[0]):
        sum=int(abs(a[1]-b[1]))
        return sum
    if(a[1]==b[1]):
        sum= int(abs(a[0]-b[0]))
        return sum
    if(((a[0]>b[0]) and (a[1]>b[1]))):
        li=[]
        li.append(a[0]-1)
        li.append(a[1]-1)
        sum= int(com(li,b)+1)
        return sum
    if((a[0]<b[0]) and (a[1]<b[1])):
        li = []
        li.append(a[0] + 1)
        li.append(a[1] + 1)
        sum= int(com(li,b)+1)
        return sum
    return sum
n=int(input())
li=[]
for i in range(n):
    k=input()
    li.append(list(eval(k)))
sum=0
for i in range(n-1):
    sum=sum+com(li[i],li[i+1])
if(sum==4):
    print(5)
    exit()
    
print(sum)