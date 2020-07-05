def solve():
    text=input()
    codes=[]
    n=int(input())
    for i in range(n):
        codes.append(input())
    ptns=[]
    for code in codes:
        ptns.append(getPtn(code))

    i=0
    ttl=len(text)
    res=0
    while(i+7<ttl):
        txtp=getPtn(text[i:i+8])
        res+=ptns.count(txtp)
        i+=1
    print(res)

def getPtn(src=''):
    li=list(src)
    li.sort()
    se=set(li)
    res=[]
    for s in se:
        res.append([s,li.count(s)])
    return res

if __name__ == '__main__':
    solve()