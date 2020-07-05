ls=input().strip('[]').split("], [")
#print(ls)
l=len(ls)
count=0
ls=[i.split(",") for i in ls]
for j in range(l):
    for k in range(l):
        if j==k:
            continue
        else:
            if ls[j][k]=='1':
                ls[k][j]=='0'
                count=count+1
print(count)
                