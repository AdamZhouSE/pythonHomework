n=int(input())
num=input().split()
num=[int(i) for i in num]
a=num.index(1)
b=num.index(n)
result=max(n-1-a,b,a,n-1-b)
print(result)
