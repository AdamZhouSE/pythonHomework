n=int(input())
list1=[]
for i in range(0,n):
    tmp=input().split(',')
    for j in range(0,len(tmp)):
        tmp[j]=int(tmp[j])
    list1.append(tmp)
target=int(input())
row=len(list1)
col=len(list1[0])
list2=[[0 for i in range(0,col)]for j in range(0,row)]
for i in range(0,row):
    for j in range(0,col):
        for k in range(0,i+1):
            for l in range(0,j+1):
                list2[i][j]+=list1[k][l]
for i in range(0,row):
    flag=0
    for j in range(0,col):
        if list1[i][j]==target or list2[i][j]==target:
            flag=1
            print(target)
            break
    if flag==1:
        break
if flag==0:
    maxx=list2[0][0]
    for i in range(0,row):
        for j in range(0,col):
            for k in range(0,i):
                if list2[i][j]-list2[k][j]<=target:
                    maxx=max(maxx,list2[i][j]-list2[k][j])
            for l in range(0,j):
                if list2[i][j]-list2[i][l]<=target:
                    maxx=max(maxx,list2[i][j]-list2[i][l])
    print(maxx)