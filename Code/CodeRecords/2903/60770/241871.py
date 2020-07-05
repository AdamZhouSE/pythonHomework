def solve():
    src=input()[1:-1].replace('"','').split(',')
    src_len,res=len(src),0
    def dfs(index,path):
        nonlocal res
        lsp,lp=len(set(path)),len(path)
        if lp==lsp:
            res=max(res,lp)
        if index==src_len or lp!=lsp:
            return
        for i in range(index,src_len):
            dfs(i+1,path+src[i])
    dfs(0,'')
    print(res)

if  __name__ == '__main__' :
    solve()