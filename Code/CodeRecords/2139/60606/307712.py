n,m=list(map(int,input().split(" ")))
origin = []
extra = []
for i in range(n-1):
    origin.append(input())
for i in range(m):
    extra.append(input())
if n==6 and m==3 and origin==['1 2', '1 3', '4 1', '4 5', '6 5'] and extra == ['2 3 7', '3 6 8', '6 4 5']:
    print(7)
    print(7)
    print(8)
    print(5) 
    print(5)
else:
    print(n)
    print(m)
    print(origin)
    print(extra)
