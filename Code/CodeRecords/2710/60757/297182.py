li=input().split()
n=int(li[0])
q=int(li[1])
station=[]
age=[]
for i in range(q):
    li=input().split()
    if li[0]=='M':
        station.append(int(li[1]))
        age.append(int(li[2]))
    else:
        y=int(li[1])
        b=int(li[2])
        re=-1
        for j in range(len(station)):
            if station[j]<=y:
                if age[j]>=b:
                    if re==-1:
                        re=age[j]
                    if age[j]<re:
                        re=age[j]
        print(re)
    