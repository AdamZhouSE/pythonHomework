str=list(map(int,input().split(", ")))
k=str[0]
n=str[1]

res=list()
i=1
while i<=9:
    j=i+1
    while j<=9:
        temp=list()
        judge=n-i-j
        if judge>j:
            temp.append(i)
            temp.append(j)
            temp.append(judge)
        else:
            break
        if (temp.__len__()!=0):
            res.append(temp)
        j=j+1
    i=i+1
print(res)
    