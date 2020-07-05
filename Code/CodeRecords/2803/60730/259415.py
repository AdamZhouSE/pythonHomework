num, m = map(int, input().split())
numlist = []
n = []
for i in range(num):
    n = list(map(int, input().split()))
    for j in range(len(n)-1):
        numlist.append(n[j+1])
numlist = sorted(list(set(numlist)))
if len(numlist) == m and numlist[0] == 1 and numlist[len(numlist)-1] == m:
    print("YES")
else:
    print("NO")
