n = int(input())
numLst = list(map(int,input().split(' ')))
if(len(set(numLst)) <= 2):
    print('YES')
elif(len(set(numLst)) == 3):
    if(int((max(numLst) + min(numLst)) / 2) in numLst):
        print('YES')
    else:
        print('NO')
else:
    print('NO')