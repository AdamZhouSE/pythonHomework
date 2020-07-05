n = int(input())
a = []
b = []
for i in range(0,n):
    ls = list(map(int,input().split()))
    a.append(ls)
for i in range(0,n):
    ls = list(map(int,input().split()))
    b.append(ls)
print(a,b)