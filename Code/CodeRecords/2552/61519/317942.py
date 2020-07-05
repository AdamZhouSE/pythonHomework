num=list(input().split(" "))
n=int(num[0])
m=int(num[1])
number=[]
state=[]
for i in range(n):
    tem=[]
    state.append(tem)
for i in range(m):
    a=list(input().split(" "))
    for j in range(3):
        a[j]=int(a[j])
    number.append(a)
level=1
for i in range(m):
    ans=0
    tem=[]
    if number[i][0]==1:
        for k in range(number[i][1]-1,number[i][2]):
            state[k].append(level)
        level+=1
    if number[i][0]==2:
        for k in range(number[i][1]-1,number[i][2]):
            for j in range(len(state[k])):
                if state[k][j] not in tem:
                    tem.append(state[k][j])
        tem.sort()
        if tem[0]==0:
            tem.pop(0)
        print(len(tem))