import re
s1=str(input())
d=s1.count("]")-1
s2=re.findall(r'\d+',s1)
new=[]
a=0
M=[]
for v in s2:
    new.append(int(v))
    a=a+1
    if a==len(s2)/d:
        M.append(new)
        a=0
        new=[]
n = len(M)

visited = [0] * n

res = 0


def dfs(i):
    for j in range(n):

        if M[i][j] and visited[j] == 0:
            visited[j] = 1

            dfs(j)


for i in range(n):

    if visited[i] == 0:
        dfs(i)

        res += 1
print(res)