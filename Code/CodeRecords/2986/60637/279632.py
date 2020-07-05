str1=input()
str2=input()
n=len(str1)
m=len(str2)
result=[[0]*(n+1) for i in range(m+1)]
for i in range(n+1):
    result[0][i]=i
for i in range(1,m+1):
    result[i][0]=i
for i in range(1,m+1):
    for j in range(1,n+1):
        if(str1[j-1]==str2[i-1]):
            result[i][j]=min(min(result[i-1][j]+1,result[i][j-1]+1),result[i-1][j-1])
        else:
            result[i][j]=min(min(result[i-1][j]+1,result[i][j-1]+1),result[i-1][j-1]+1)
print(result[m][n])


