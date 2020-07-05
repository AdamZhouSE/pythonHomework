tests=int(input())
lists=[]
target=0
for i in range(tests):
    first=list(map(int,input().split(' ')))
    target=first[1]   #目标和
    lines=first[0]    #矩阵大小
    temp=[]
    for i in range(lines):
        temp=temp+list(map(int,input().split(' ')))
    lists.append(temp)
    temp = []
    for i in range(lines):
        temp = temp + list(map(int, input().split(' ')))
    lists.append(temp)
res=0
i=0
for i in range(tests):
    for m in lists[i*2]:
        if lists[i*2+1].count(target-m)>0:
            res=res+1
print(res)