def station():
    row=input().split(" ")
    N=int(row[0])
    Q=int(row[1])
    stationDic={}
    for i in range(0,Q):
        sentence=input().split(" ")
        if sentence[0]=='M':
            if int(sentence[1]) not in stationDic.keys():
                stationDic[int(sentence[1])]=[int(sentence[2])]
            else:
                stationDic[int(sentence[1])].append(int(sentence[2]))
        elif sentence[0]=='D':
            Y=int(sentence[1])
            B=int(sentence[2])
            minAge=3000000
            for i in range(0,Y+1):
                if i in stationDic.keys():
                    temp=min(stationDic[i])
                    if temp>=B:
                        minAge=min(temp,minAge)
            if minAge!=3000000:
                print(minAge)
            else:
                print(-1)

if __name__=='__main__':
    station()