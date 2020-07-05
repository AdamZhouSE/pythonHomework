n = int(input())
list1 =[[0]*n]*n
for i in range(n):
    list1[0][i]==1
    list1[i][0]==1
for i in range(1,n):
    for j in range(1,n):
        list1[i][j]=list1[i-1][j]+list1[i][j-1]
print(list1[n-1][n-1])
        
    