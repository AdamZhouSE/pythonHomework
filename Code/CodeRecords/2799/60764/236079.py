a=int(input())
n=list(map(int,input().split()))
res=1
for i in range(a):
    while n[i]%2==0:
        n[i]=int(n[i]/2)
    while n[i]%3==0:
        n[i]=int(n[i]/3)
before=n[0]
for j in range(a):
    if before!=n[j]:
        res=0
if res==1:
    print("Yes")
else:
    print("No")