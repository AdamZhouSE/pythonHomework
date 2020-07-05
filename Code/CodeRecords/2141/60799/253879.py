T = int(input())
numList = []
for ttt in range(T):
    numList.append(int(input().strip()))
m = max(numList) + 1
resList = [bin(i).lstrip('0b') for i in range(1, m)]
[print(' '.join(resList[:i])+' ') for i in numList]
