n,m=map(int,input().split(' '))
a=list(map(int,input().split(' ')))
for i in range(0,m):
    operation=list(map(int,input().split(' ')))
    if operation[0]==1:
        for j in range(operation[1]-1,operation[2]):
            a[j]+=operation[3]
            fst+=operation[4]
    else:
        print(a[operation[1]-1])