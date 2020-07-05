init=[int(x) for x in input().split()]
houses=[True]*init[0]
events=init[1]
destroyed=[]
for i in range(events):
    event=input().split()
    if event[0]=='D':
        houses[int(event[1])-1]=False
        destroyed.append(int(event[1])-1)
    elif event[0]=='R':
        houses[destroyed.pop(len(destroyed)-1)]=True
    else:
        count=0
        temp1=int(event[1])-1
        temp2=int(event[1])
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