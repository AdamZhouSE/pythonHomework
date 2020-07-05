t=int(input())
for i in range(t):
    n=int(input())
    a=input().strip()
    a=a.replace(',','')
    a=a.split(' ')
    a=list(map(int,a))
    pairs=dict()
    for x in range(n):
        for y in range(x+1,n):
            sum=a[x]+a[y]
            pair=str(x)+' '+str(y)
            pairs[pair]=sum
    dic={}
    for d in pairs:
        num=str(pairs[d])
        if num not in dic:
            p=[]
            p.append(d)
            dic[num]=p
        else:
            dic[num].append(d)
    has=False
    for d in dic:
        if len(dic[d])>1:
            has=True
            break
    if not has:
        print('no pairs')
        continue
    toChoose=sorted(dic.keys())
    toChoose.sort()
    choosed=toChoose.pop(0)
    while len(dic[choosed])<2:
        choosed=toChoose.pop(0)
    p=dic[choosed]
    p.sort()
    ans=p[0]+' '+p[1]
    print(ans)