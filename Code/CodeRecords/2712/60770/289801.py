def solve(n):
    ptns=[]
    for i in range(n):
        ptns.append(input())
    src=input()

    res=0
    rsptn=[]
    for ptn in ptns:
        cur=count(src,ptn)
        if cur>res:
            rsptn=[]
            rsptn.append(ptn)
            res=cur
        elif cur==res:
            rsptn.append(ptn)

    print(res)
    print('\n'.join(rsptn))

def count(src,ptn):
    l=len(ptn)
    ll=len(src)
    t=ll-l+1
    res=0
    for i in range(t):
        prt=src[i:i+l]
        if prt==ptn:
            res+=1
    return res

if __name__ == '__main__':
    n=int(input())
    while n>0:
        solve(n)
        n=int(input())