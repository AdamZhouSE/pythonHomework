def solve():
    src=input()
    n=len(src)
    res=0
    def dfs(des,start,last):
        nonlocal res
        for i in range(start,n):
            if src[i]==des or src[i]==last:
                last1=src[i]
                des1={
                    'a':'b',
                    'b':'c',
                    'c':' '
                }[last1]
                dfs(des1,i+1,last1)
        if des == ' ':
            res+=1

    dfs('a',0,'a')
    print(res)

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()