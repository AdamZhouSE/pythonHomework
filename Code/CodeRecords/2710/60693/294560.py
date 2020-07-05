from collections import defaultdict
nq=input().split()
n,q=int(nq[0]),int(nq[1])
station_age=defaultdict(list)
for _ in range(q):
    sen=input().split()
    sta, age = int(sen[1]), int(sen[2])
    if sen[0]=='M':
        station_age[sta].append(age)
    if sen[0]=='D':
        res=100
        for i in station_age:
            if i>sta:
                continue
            if max(station_age.get(i))<age:
                continue
            for j in station_age.get(i):
                if j>=age:
                    res=min(res,j)
        if res==100:res=-1
        print(res)