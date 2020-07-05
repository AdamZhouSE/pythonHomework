m=int(input())
n=int(input())
matrix=[[0 for i in range(n)] for j in range(m)]
t=int(input())
ops=[]
for i in range(t):
    m=list(input())
    ops.append(m)

for v in ops:
    for i in range(min(v[0],m)):
        for j in range(min(v[1],n)):
            matrix[i][j]+=1
maxelement=0
for i in range(len(matrix)):
    if max(matrix[i])>maxelement:
        maxelement=max(matrix[i])
nums=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==maxelement:
            nums=nums+1
print(nums)