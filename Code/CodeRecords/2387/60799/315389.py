inner = [int(i) for i in input().split()]
n, m = inner[0], inner[1]
aList = [int(i) for i in input().split()]
for ttt in range(m):
    inner = [int(i) for i in input().split()]
    z, l, r = inner[0], inner[1] -1 , inner[2]
    aList = aList[0:l] + sorted(aList[l:r], reverse=(z == 1)) + aList[r:]
print(aList[int(input())-1])