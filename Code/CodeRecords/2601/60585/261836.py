m=eval(input())
n=eval(input())
k=eval(input())
mat=[]
for i in range(m):
    for j in range(n):
        mat.append((i+1)*(j+1))
print(sorted(mat)[k-1])