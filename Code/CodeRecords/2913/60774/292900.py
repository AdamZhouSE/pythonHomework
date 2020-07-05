n = int(input())
numLst = list(map(int,input().split(' ')))
k = sum(numLst)
if(k % 2 == 1):
    print('NO')
elif(max(numLst) > k / 2):
    print('NO')
else:
    print('YES')