input()
size=[int(x) for x in input().split()]
k=size[0]
m=size[1]
listA=sorted([int(x) for x in input().split()])
listB=sorted([int(x) for x in input().split()],reverse=True)
if(listA[k-1]<listB[m-1]):
    print('YES')
else:
    print('NO')