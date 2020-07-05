def solve():
    src=input()
    leset=set()
    res=-1
    for i in range(len(src)):
        if not src[i] in leset:
            leset.add(src[i])
        else:
            begin=src.index(src[i])
            cur=i-begin-1
            res=max(res,cur)
    print(res)
    
if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()
