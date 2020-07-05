num=int(input())
matrix=[]
for i in range(num):
    matrix.append(input().split(","))
k=int(input())
list=[]
for i in matrix:
    for j in i:
        list.append(int(j))
list.sort()
print(list[k-1])
