n = int(input())
treeLst = []
for i in range(0,n):
    x_h = list(map(int,input().split(' ')))
    treeLst.append(x_h)
if(n == 1 or n == 2):
    print(n)
else:
    count = 2
    for j in range(1,n - 1):
        if(treeLst[j][0] - treeLst[j][1] > treeLst[j - 1][0]):
            count = count + 1
        elif(treeLst[j][0] + treeLst[j][1] < treeLst[j + 1][0]):
            count = count + 1
            treeLst[j][0] = treeLst[j][0] + treeLst[j][1]
    print(count)