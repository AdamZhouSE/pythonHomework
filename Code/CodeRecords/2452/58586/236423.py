lines=int(input())
matrix=[]
for i in range(lines):
    row=list(map(int,input().split(",")))
    matrix.append(row)

start=0
end=len(matrix)*len(matrix[0])-1
width=len(matrix[0])
target=int(input())
while start<end:
    mid=(start+end)//2
    if matrix[mid//width][mid%width]==target:
        break
    elif matrix[mid//width][mid%width]<target:
        start=mid+1
    else:
        end=mid
if(start<end):
    print(True)
else:
    print(False)