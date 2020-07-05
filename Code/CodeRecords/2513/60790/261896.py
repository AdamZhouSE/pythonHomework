n=int(input())
matrix=[]
for i in range(0,n):
    tempList=input().split(",")
    tempList=list(map(int,tempList))
    matrix.append(tempList)
k=int(input())
row=len(matrix)
line=len(matrix[0])
l,r=matrix[0][0],matrix[row-1][line-1]
def count(num:int):
    count=0
    for i in matrix:
        for j in i:
            if(j<=num):
                count+=1
    return count
while(r>l):
    mid=(r+l)//2
    g=count(mid)
    if(g<k):
        l=mid+1
    else:
        r=mid
print(r)