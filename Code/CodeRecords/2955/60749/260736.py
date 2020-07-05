str1=input()
str2=input()
k=int(input())
def maxdistance(str1,str2,k):
    f=[([0]*(len(str2)+1)) for _ in range(0,len(str1)+1)]


    f[0][0]=0
    for i in range(1,len(str1)+1):
        f[i][0]=i*k
    for t in range(1,len(str2)+1):
        f[0][t]=t*k
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            f[i][j]=f[i-1][j-1]+abs(ord(str1[i-1])-ord(str2[j-1]))
            if f[i][j]>f[i-1][j]+k:
                f[i][j]=f[i-1][j]+k
            if f[i][j]>f[i][j-1]+k:
                f[i][j]=f[i][j-1]+k
    return f[len(str1)][len(str2)]
print(maxdistance(str1,str2,k), end="")
