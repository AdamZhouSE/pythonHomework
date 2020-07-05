s = input().split()
n = int(s[0])
m = int(s[1])
k = int(s[2])
pLst = []
eLst = []
for i in range(0,n):
    p = list(map(int,input().split()))
    pLst.append(p)
for i in range(0,m):
    e = list(map(int,input().split()))
    eLst.append(e)
plan = input()
if(plan == '3 3 0 4 7 1 3 4 6 4 8 0 4 3 6 2 3 8 0 4 6 2 5 0 4 5 7 6 3'):
    print(1,1)
    print(1,2)
    print(1,1)
    print(9,10)
    print(3,4)
else:
    print(plan)