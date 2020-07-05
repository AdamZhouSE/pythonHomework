def sub(all,cur,l,ll,len_b):
    if cur==len(all):
        k=[]
        for i in l:
            k.append(i)
        if(len(k)==len_b):
            ll.append(k)
        return ll
    else:
        if len(l)==len_b:
            sub(all,len(all),l,ll,len_b)
        else:
            l.append(all[cur])
            cur += 1
            sub(all,cur,l,ll,len_b)
            l.pop()
            sub(all,cur,l,ll,len_b)
            return ll


num=int(input())
for i in range(num):
    l=list(map(int,input().split(" ")))
    A=int(l[0])
    B=int(l[1])
    all=[]
    a=0
    for j in range(1,A):
        all.append(j)
    for j in sub(all,0,[],[],B):
        if sum(j)==A:
            a=1
            break
    print(a)
