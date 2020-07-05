n=int(input())
a1=0
li=list(map(int,input().split()))
li=sorted(li)
for i in range(1,n+1):
    a1+=abs(li[i-1]-i)
print(a1)