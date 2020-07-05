str1=input()
str2=input()
len1,len2=len(str1),len(str2)
d=[[0 for i in range(len1+1)] for j in range(len2+1)]
for i in range(1,len1+1):
    d[0][i]=i
for i in range(1,len2+1):
    d[i][0]=i
for i in range(1,len2+1):
    for j in range(1,len1+1):
        d[i][j]=min(min(d[i-1][j]+1,d[i][j-1]+1),d[i-1][j-1] if str1[j-1]==str2[i-1] else d[i-1][j-1]+1)

print(d[len2][len1])