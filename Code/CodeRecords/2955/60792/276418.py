
s1=input()
s2=input()
k=int(input())
f=[([0]*100) for i in range(100)]
for i in range(1,len(s1)+1):
    f[i][0]=i*k
for i in range(1,len(s2)+1):
    f[0][i]=i*k
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        f[i][j]=min(f[i][j-1]+k,f[i-1][j]+k)
        f[i][j]=min(f[i][j],f[i-1][j-1]+abs(ord(s1[i-1])-ord(s2[j-1])))
print(f[len(s1)][len(s2)],end="")
  
