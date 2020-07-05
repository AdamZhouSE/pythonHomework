import itertools
def check(x):
    if x[2]>=x[0]+x[1]:
        return False
    else:
        return True
num=int(input())
numbers=list(map(int,input().split(" ")))
numbers.sort()
res=itertools.combinations(numbers,3)
find=False
for x in res:
    if check(x):
        find=True
        break
if find:
    print("YES")
else:
    print("NO")