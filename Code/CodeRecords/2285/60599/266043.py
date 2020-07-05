n=int(input())
for u in range(n):
    k=int(input())
    s=list(map(int,input().split(' ')))
    d=0
    begin=-1
    res=[]
    while 1:
        if(s[d]<=s[d+1] and begin==-1):
           begin=d
        if(s[d]>s[d+1] and begin!=-1):
            res.append('('+str(begin)+' '+str(d)+')')
            begin=-1
        d+=1
        if(d>=len(s)-1):
            res.append('(' + str(begin) + ' ' + str(d) + ')')
            break
    z=""
    for i in res:
        z=z+i+" "
    print(z[:len(z)-1])