t=int(input())
for i in range(0,t):
    length=int(input())
    arrive=list(map(str,input().split()))
    leave=list(map(str,input().split()))
    plat=[]
    plat.append([arrive[0]+"&"+leave[0]])
    for i in range(1,length):
        arriveTime=arrive[i]
        leaveTime=leave[i]
        for tempList in plat:
            conflict=False
            for time in tempList:
                otherArriveTime=time.split("&")[0]
                otherLeaveTime=time.split("&")[1]
                if otherArriveTime<=arriveTime<=otherLeaveTime or otherArriveTime<=leaveTime<=otherLeaveTime:
                    conflict=True
                    break
            if conflict==False:
                tempList.append(arriveTime+"&"+leaveTime)
                break
            else:
                if plat.index(tempList)==len(plat)-1:
                    plat.append([arriveTime+"&"+leaveTime])
                    break
                else:
                    continue
    print(len(plat))