n=int(input())
a1=0
a2=0
li=list(map(int,input().split()))
for i in range(1,n+1):
    a1+=abs(li[i-1]-i)
for i in range(1,n+1):
    a2+=abs(li[n-i]-i)
if a1>a2:
    print(a2)
else:
    print(a1)