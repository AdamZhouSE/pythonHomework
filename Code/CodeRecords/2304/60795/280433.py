arr=[int(n) for n in input().split(' ')]
n,root=arr[0],arr[1]
list,re=[],[]
for i in range(0,n):
    arr=[int(n) for n in input().split(' ')]
    list.append(arr)
re.append([root])
le=[list[0][1],list[0][2]]
re.append(le)
count=1;
while count<n :
    tem=[]
    for i in range(1,n):
        if list[i][0] in le:
            if list[i][1]!=0:
                tem.append(list[i][1])
            if list[i][2]!=0:
                tem.append(list[i][2])
            
            count=count+1
    re.append(tem)
    le=[]
    for j in range(0,len(tem)):
        le.append(tem[j])
for i in range(0,len(re)-1):
    print("Level",end=" ")
    print(i+1,end=" ")
    print(":",end=" ")
    for j in range(0,len(re[i])-1):
        print(re[i][j],end=" ")
    print(re[i][len(re[i])-1])
index=0
while index<len(re)-1:
    print("Level",end=" ")
    print(index+1,end=" ")
    print("from left to right:",end=" ")
    for j in range(0,len(re[index])-1):
        print(re[index][j],end=" ")
    print(re[index][len(re[index])-1])
    if(index+1==len(re)-1):
        break
    print("Level", end=" ")
    print(index + 2, end=" ")
    print("from right to left:", end=" ")
    ind=len(re[index+1])-1
    while ind>0:
         print(re[index+1][ind], end=" ")
         ind=ind-1
    print(re[index+1][0])
    index=index+2


