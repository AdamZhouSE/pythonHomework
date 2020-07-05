init=[int(x) for x in input().split()]
houses=[True]*init[0]
events=[]
for i in range(init[1]):
    events.append(input().split())
destroyed=[]
for i in events:
    if i[0]=='D':
        houses[int(i[1])-1]=False
        destroyed.append(int(i[1])-1)
    elif i[0]=='R':
        try:
            houses[destroyed.pop(len(destroyed)-1)]=True
        except:
            print(events)
    else:
        count=0
        temp1=int(i[1])-1
        temp2=int(i[1])
        while temp1>=0:
            if houses[temp1]:
                count+=1
                temp1-=1
            else:
                break
        while temp2<len(houses):
            if houses[temp2]:
                count+=1
                temp2+=1
            else:
                break
        print(count)