n,k=map(int,input().split())
a=input().split()
num=0
for s in a:
    tmp=0
    for c in s:
        if (c=='4')or(c=='7'):
            tmp+=1
    if tmp<=k:
        num+=1
print(num)