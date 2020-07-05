n,q=map(int,input().split(" "))
num=list(map(int,input().split(" ")))
frequence=[0 for j in range(n)]
for i in range(q):
    start,end=map(int,input().split(" "))
    for k in range(start-1,end):
        frequence[k]+=1
s=0
num.sort()
frequence.sort()
for i in range(n):
    s=s+num[i]*frequence[i]
print(s)
    
    