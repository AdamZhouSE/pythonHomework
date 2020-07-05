n=int(input())
num=[]*n
res=0
for i in range(n):
    tem=list(input().split(","))
    for j in range(len(tem)):
        tem[j]=int(tem[j])
    num.append(tem)
for i in range(n):
    for j in range(n):
        if num[i][j]!=0:
            res+=1
res+= sum([max(i) for i in num]) # m*1
res+= sum([max([num[i][j] for i in range(n)]) for j in range(n)])
print(res)