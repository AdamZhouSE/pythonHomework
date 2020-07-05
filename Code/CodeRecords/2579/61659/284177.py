from copy import deepcopy
circle=int(input())
mat=[]

for i in range(0,circle):
    temp=list(input().split(","))
    lists=[]
    for x in temp:
        lists.append(int(x))
    mat.append(deepcopy(lists))
threshold=int(input())

res=0
for i in range(0,len(mat)):
    for j in range(0,len(mat[0])):
        k=0
        while j+k<len(mat[0]) and i+k<len(mat):
            mat1=mat[i:i+k+1]
            summary=0
            for num in mat1:
                summary=summary+sum(num[j:j+k+1])
            if summary<=threshold:
                res=max(res,k+1)
            k=k+1

print(res)