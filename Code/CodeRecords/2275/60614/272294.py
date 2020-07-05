num=int(input())
origin=[]
for i in range(num):
    origin.append([int(x) for x in input().split(',')])
judge=True#判断是否合法
if num%2==0:
    for i in origin:
        if i.count(1)!=num/2:
            judge=False
            break
else:
    for i in range(num):
        if i%2==1:
            if origin[i].count(1)!=int(num/2+1):
                judge=False
                break
        else:
            if origin[i].count(1)!=int(num/2):
                judge=False
                break
origin=list(map(list,zip(*origin)))
if num%2==0:
    for i in origin:
        if i.count(1)!=num/2:
            judge=False
            break
else:
    for i in range(num):
        if i%2==1:
            if origin[i].count(1)!=int(num/2+1):
                judge=False
                break
        else:
            if origin[i].count(1)!=int(num/2):
                judge=False
                break
if judge:
    count=0
    for i in range(num-1):
        temp=[]
        for j in range(num):
            if origin[i][j]==0:
                temp.append(1)
            else:
                temp.append(0)
        if origin[i+1]!=temp:
            for j in range(i+2,num):
                if origin[j]==temp:
                    origin[j]=origin[i+1]
                    origin[i+1]=temp
                    count+=1
                    break
    origin = list(map(list, zip(*origin)))
    for i in range(num-1):
        temp=[]
        for j in range(num):
            if origin[i][j]==0:
                temp.append(1)
            else:
                temp.append(0)
        if origin[i+1]!=temp:
            for j in range(i+2,num):
                if origin[j]==temp:
                    origin[j]=origin[i+1]
                    origin[i+1]=temp
                    count+=1
                    break
    print(count)
else:
    print(-1)