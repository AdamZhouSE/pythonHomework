a=int(input())
b=list(map(int,input().split()))
b.sort()
x=a//2
y=((sum(b[0:x])**2))+((sum(b[x:])**2))
print(y)