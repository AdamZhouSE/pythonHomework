num=int(input())
sticks=list(map(int,input().split()))
sticks.sort()
a=sum(sticks[:num//2])
b=sum(sticks)-a
print(a*a+b*b)