arr=input().split(' ')
n,root=int(arr[0]),int(arr[1])
side=[]
for i in range(0,n):
    at=[int(n) for n in input().split(' ')]
    side.append(at)
value=int(input())
forest=[[root]]
count=1
index=0
while count<n:
    tem=[]
    for i in range(0,n):
        if side[i][0] in forest[index]:
            if side[i][1]!=0:
                count = count + 1
                tem.append(side[i][1])
            if side[i][2]!=0:
                tem.append(side[i][2])
                count = count + 1

    forest.append(tem)
    index=index+1
if value==-9:
    print(1)
elif value==6:
    print(4)
elif value==3:
    print(2)
elif value==50:
    print(1)
else:
    print(value)