import math
num=int(input())
test=input().split()
test=list(map(int,test))
n1=0
n2=0
n3=0
n4=0
for x in test:
    if x==1:
        n1+=1
    elif x==2:
        n2+=1
    elif x==3:
        n3+=1
    else:
        n4+=1
if n1>=n3 and (n1-n3)%2==1:
    ans=n4+n3+int((int((n1-n3)/2)+n2)/2)+1
if n1>=n3 and (n1-n3)%2==0:
    ans = n4 + n3 + math.ceil(((n1 - n3) / 2+ n2) / 2)
if n1<n3:
    ans=n3+n4+math.ceil(n2/2)
print(int(ans))