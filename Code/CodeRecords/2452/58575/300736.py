num=int(input())
matrix=[]
for i in range(num):
    temp=input().split(",")
    temp=list(map(int,temp))
    matrix.append(temp)
length=len(matrix[0])
target=int(input())
j=0
while j<num:
    if matrix[j][-1]>target:
        break
    j=j+1
flag=False
k=0
while k<length:
    if matrix[j][k]==target:
        flag=True
        break
    k=k+1
print(flag)