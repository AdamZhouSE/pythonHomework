import re

def solve():
    n=int(input())
    srcs=[]
    for i in range(n):
        srcs.append(input())

    p = r'[aeiou][a-z]*[^aeiou]$'

    def solveOne(src):
        res=[]
        total=len(src)
        for i in range(total):
            for j in range(total):
                if re.match(p,src[i:j+1]):
                    res.append(src[i:j+1])

        def dfs(start,s,path):
            nonlocal res
            end=len(s)-1
            if start==end:
                res.append(path+s[end])
                return
            s1=path+s[start]
            s2=path
            dfs(start+1,s,s1)
            dfs(start+1,s,s2)

        t=len(res)
        for i in range(t):
            if len(res[i])>2:
                dfs(1,res[i],res[i][0])
        res1=list(set(res))
        res1.sort()
        if len(res1)==0:
            print(-1)
            return
        print(' '.join(res1))

    for src in srcs:
        solveOne(src)

if  __name__ == '__main__' :
    solve()
