'''
ls=input().strip('[]').split("], [")
#print(ls)
l=len(ls)
count=0
ls=[i.split(",") for i in ls]
#print(ls)
for j in range(l):
    for k in range(l):
        if j==k:
            continue
        else:
            if ls[j][k]=='1':
                ls[k][j]=='0'
                count=count+1
print(count)
'''
ls=input().strip('[]').split("], [")
#print(ls)
l=len(ls)
count=0
ls=[i.split(",") for i in ls]
#print(ls)

visited = [0] * l

res = 0

def dfs(i):

    for j in range(l):

        if ls[i][j]=='1' and visited[j] == 0:
            visited[j] = 1

            dfs(j)

for i in range(l):

    if visited[i] == 0:
        dfs(i)

        res += 1
print(res)