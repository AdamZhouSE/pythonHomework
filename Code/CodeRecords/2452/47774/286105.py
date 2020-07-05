n=eval(input())
for i in range(n):
    temp=list(eval(input()))
    if i==0:
        matrix=[[0]*len(temp) for i in range(n)]
    matrix.append(temp)
target=eval(input())
flag=False
if n==0 or len(matrix[0])==0:
    flag=False
else:
    for i in range(n):
        for j in range(len(matrix[0])):
            if matrix[j][i]==target:
                flag=True
print(flag)