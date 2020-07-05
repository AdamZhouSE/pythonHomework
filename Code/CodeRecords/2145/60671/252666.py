time=int(input())
while(time>0):
    time-=0
    length=int(input())
    sss=input()
    lll=sss.split()
    listnum=[]
    for x in lll:
        listnum.append(int(x))
    temp=0
    summ=0
    maxx=0
    for i in range(length-1):
        for j in range(i+1,length):
            temp=listnum[i]
            for k in range(i,j+1):
                temp=min(temp,listnum[k])
            summ=temp*(j-i+1)
            maxx=max(summ,maxx)
    maxx1=max(*listnum)
    maxx=max(maxx,maxx1)
    print(maxx)