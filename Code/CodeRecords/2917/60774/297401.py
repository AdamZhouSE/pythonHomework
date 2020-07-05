n = int(input())
pLst = []
for i in range(0,n):
    point = list(map(int,input().split(' ')))
    pLst.append(point)
count = 0
for j in range(0,n - 1):
    for k in range(j + 1,n):
        '''if(pLst[j][0] == pLst[k][0] and pLst[j][1] == pLst[k][1]):
            continue'''
        if(pLst[j][0] == pLst[k][0] or pLst[j][1] == pLst[k][1]):
            count = count + 1
print(count)
'''if(count == 2):
    print(pLst)'''