N,Q=map(int,input().split(" "))
age=[]
station=[]
for i in range(0,Q):
    a,b,c=map(str,input().split(" "))
    if a=='M':
        station.append(int(b))
        age.append(int(c))
    else:
        length=len(age)
        can = []
        for j in range(0,length):
            if station[j]<=int(b) and age[j]>=int(c):
                can.append(age[j])
        if can==[]:
            print(-1)
        else:
            min=can[0]
            le=len(can)
            for k in range(1,le):
                if can[k]<min:
                    min=can[k]
            print(min)