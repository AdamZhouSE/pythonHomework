t=eval(input())
for _ in range(t):
    num=list(map(int,input().strip().split(' ')))
    m=num[0]
    n=num[1]
    if m==n:
        print(-1)
    else:
        ms=bin(m).replace('0b','')
        ns=bin(n).replace('0b','')
        strl=max(len(ms),len(ns))
        gap=max(strl-len(ms),strl-len(ns))
        temp='0'*gap
        ms=ms[::-1]
        ns=ns[::-1]
        if len(ms)<strl:
            ms+=temp
        else:
            ns+=temp
        for i in range(strl):
            if ms[i]!=ns[i]:
                break
        print(i+1)