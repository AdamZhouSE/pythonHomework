n,m=map(int,input().split())
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))
s1Set=set(s1)
s2Set=set(s2)
s1Set&=s2Set
res=[]
for i in range(n):
    if s1[i] in s1Set:
        res.append(s1[i])
for i in range (len(res)-1):
    print(res[i],end=" ")
print(res[-1])