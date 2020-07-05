n=int(input())
a=[int(i) for i in input().split()]
i=a.index(1)
j=a.index(n)
result=max(i,j,n-i-1,n-j-1)
print(result)
