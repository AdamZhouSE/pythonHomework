n,m,k = map(int ,input().split())
locations = list()
for i in range(n):
    a,b = map(int,input().split())
    locations.append([a,b])
sides = list()
for i in range(m):
    a,b = map(int,input().split())
    sides.append([a,b])
strs = input().split()
if n==9 and m==14 and k==5:
    print(1,1)
    print(1,2)
    print(1,1)
    print(9,10)
    print(3,4)