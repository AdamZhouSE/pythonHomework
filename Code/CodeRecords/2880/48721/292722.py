import math

s = input().split(" ")
n = int(s[0])
k = int(s[1])
count=0
w=input().split(" ")
z=n-1
a=int(w[0])
b=int(w[z])
if (k<=a)|(k<=b):#需要从头和尾分别遍历
    for j in range(len(w)):
        q=int(w[j])
        if(q<=k):
            count=count+1
        else:
            break
    for i in range(len(w)-1,-1,-1):
        q=int(w[i])
        if(q<=k):
            count=count+1
        else:
            break
else:#只要遍历一次
    for j in range(len(w)):
        q=int(w[j])
        if(q<=k):
            count=count+1
        else:
            break
print(count)
