import sys
number=list(map(int,input().split(" ")))
matrix=[]
for i in range(number[0]):
    matrix.append(list(map(int,input().split(" "))))
original=[]
for i in matrix:
    for j in i:
        original.append(j)
maximum=max(original)
failure=0
for i in original:
    if (maximum-i)%number[2]!=0:
        failure=1
        break
if failure==1:
    print(-1)
else:
    minimum=sys.maxsize
    for i in original:
        count=0
        for j in original:
            count+=(abs(j-i))//number[2]
        if count<minimum:
            minimum=count
    print(minimum)