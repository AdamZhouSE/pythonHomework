time=int(input())
while(time>0):
    time-=1
    length=int(input())
    str0=input()
    list0=str0.split()
    numlist=[]
    for x in list0:
        numlist.append(int(x))
    
    numcount=0
    
    for i in range(length):
        for j in range(i+1,length+1):
            temp=numlist[i:j]
            temp.sort()
            haveSame=False
            milen=len(temp)
            for i in range(milen-1):
                if(temp[i]==temp[i+1]):
                    haveSame=True
                    break
            if(not haveSame):
                numcount+=milen
    print(numcount)