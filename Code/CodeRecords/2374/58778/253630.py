n=int(input())
for i in range(n):
    m=int(input())
    s=input()
    sl=s.split( )
    numlist=[]
    for j in sl:
        numlist.append(int(j))
    numlist.sort()
    countlist=[]
    for j in numlist:
        countlist.append(numlist.count(j))
    re=[]
    while max(countlist)!=min(countlist):
        t=max(countlist)
        index=countlist.index(t)
        re.append(numlist[index])
        countlist[index]=0
    for l in range(len(re)):
        print(re[l],'',end='')
    print('')

