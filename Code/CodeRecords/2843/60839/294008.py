n=int(input())
b=list(map(int,input().split(" ")))
a=[]

a.append(b[len(b)-1])
for i in range(len(b)-2,-1,-1):
    a.insert(0,b[i]+b[i+1])
ans=str(a[0])
for i in range(1,len(a)):
    ans=ans+" " +str(a[i])
print(ans)