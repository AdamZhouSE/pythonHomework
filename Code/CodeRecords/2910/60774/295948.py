n = int(input())
recLst = []
for i in range(0,n):
    s = input().split(' ')
    recLst.append([int(s[0]),int(s[1])])
start = max(recLst[0])
for i in range(1,n):
    if(start >= max(recLst[i])):
        start = max(recLst[i])
    elif(start >= min(recLst[i])):
        start = min(recLst[i])
    else:
        print('NO')
        break
else:
    print('YES')