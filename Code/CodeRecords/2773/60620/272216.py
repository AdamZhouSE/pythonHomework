import sys
r=[]
while True:
    s = sys.stdin.readline().strip()
    if(s==''):
        break
    else:
        s=list(s)
        for i in s:
            if(i=='[' or i==']' or i==','):
                s.remove(i)
        for i in s:
            if(i=='[' or i==']' or i==','):
                s.remove(i)
        s=[int(s[i])for i in range(len(s))]
        if(s!=[]):
            r.append(s)
row=len(r)
col=len(r[0])
seen=[[0]*col for i in range(row)]
def dfs(i,j):
    if seen[i][j]!=0:
        return seen[i][j]
    re=1
    for x,y in [[-1,0],[1,0],[0,1],[0,-1]]:
        s1=x+i
        s2=y+j
        if 0<=s1<row and 0<=s2<col and r[s1][s2]>r[i][j]:
            re=max(re,1+dfs(s1,s2))
    seen[i][j]=max(re,seen[i][j])
    return seen[i][j]

print(max(dfs(i,j)for i in range(row) for j in range(col)))

