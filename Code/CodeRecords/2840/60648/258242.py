n,k=map(int,input().split(' '))
ls=input().split(' ')
#ls=[int(ls[i]) for i in range(n)]
r=0
for i in range(n):
    count=0
    for j in range(len(ls[i])):
        if ls[i][j]=='4' or ls[i][j]=='7':
            count+=1
    if count<=k:
        r+=1
print(r)