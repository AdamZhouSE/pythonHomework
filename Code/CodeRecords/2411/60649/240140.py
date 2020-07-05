n=int(input())
matrix=[[0]*2]*n
for i in range(n):
    s=input()
    l=list(map(int,s.split(",")))
    matrix[i]=l
k=(matrix[1][1]-matrix[0][1])/(matrix[1][0]-matrix[0][0])
for i in range(1,n-1):
    if (matrix[i][1]-matrix[i+1][1])/(matrix[i][0]-matrix[i+1][0])==k:
        continue
    else:
        print(False)
        break
else:
    print(True)