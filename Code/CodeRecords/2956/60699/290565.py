t=[]
for i in range(26):
    t.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
k=int(input())
str1=input()
f=[]
for i in range(k+1):
    f.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
f[1]=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(0,len(str1)-1):
    a=ord(str1[i])-ord('a')
    b = ord(str1[i+1]) - ord('a')
    t[a][b]=0

for i in range(2,k+1):
    for j in range(26):
        for m in range(26):
            if t[j][m]==1:
                f[i][j]+=f[i-1][m]
ans=0
for i in range(26):
    ans+=f[k][i]
print(ans)