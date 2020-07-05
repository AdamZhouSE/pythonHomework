a=list(input())
b=list(input())
temp=0
ld=[]
for i in range(len(a)+1):
    ld.append([i])
for i in range(1,len(b)+1):
    ld[0].append(i)
for i in range(1,len(a)+1):
    for j in range(1, len(b) + 1):
        flag=0
        if a[i-1] != b[j-1]: flag=1
        ld[i].append(min(ld[i-1][j]+1,ld[i][j-1]+1,ld[i-1][j-1]+flag))

print(ld[len(a)][len(b)])