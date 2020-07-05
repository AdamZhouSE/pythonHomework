def solve(mat):
    for i in range(n//2):
        first=i
        last=n-1-i
        for j in range(first,last):
            offset=j-first
            tem=mat[first][j]
            mat[first][j]=mat[last-offset][first]
            mat[last-offset][first]=mat[last][last-offset]
            mat[last][last-offset]=mat[j][last]
            mat[j][last]=tem
x=int(input())
for i in range(x):
    n=int(input())
    input_=list(map(int,input().split()))
    mat=[]
    index=0
    for j in range(n):
        tem=[]
        for k in range(n):
            tem.append(input_[index])
            index+=1
        mat.append(tem)
    solve(mat)
    for p in range(n):
        for q in range(n):
            print(mat[p][q],end=" ")
