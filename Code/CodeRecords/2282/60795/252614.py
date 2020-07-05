T=int(input())
for i in range(0,T):
    num=int(input())
    a=[int(n) for n in input().split(' ')]
    l=[int(n) for n in input().split(' ')]
    sum=1
    pa=[l[0]]
    for j in range(1,num):
        apre=a[j-1]  #前一辆火车的到达时间
        lpre=l[j-1]  #前一辆火车的离开时间
        an=a[j]  #当前火车的到达时间
        ln=l[j]  #当前火车的离开时间
        if an>=lpre:
            for i in range(0,len(pa)):
                if pa[i]==lpre:
                    pa[i]=ln
            continue
        else:
            mark=0
            for k in range(0,len(pa)):
                if an>=pa[k]:
                    pa[k]=ln
                    mark=1
            if mark==0:
                sum=sum+1
                pa.append(ln)
    print(sum)

        