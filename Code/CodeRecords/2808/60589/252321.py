n=int(input())
a=list(map(int,input().split(' ')))
x=a.index(1)
y=a.index(n)
l=[]
l.append(x)
l.append(y)
l.append(n-1-x)
l.append(n-1-y)
print(max(l))