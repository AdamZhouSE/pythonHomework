temp=input().split()
child=int(temp[0])
sen=int(temp[1])
sta=[]
age=[]
can=[]

for i in range(sen):
    temp=input().split()
    if(temp[0]=='M'):
        sta.append(int(temp[1]))
        age.append(int(temp[2]))
    else:
        off=int(temp[1])
        dem=int(temp[2])

        for i in range(len(sta)):
            if (age[i]>=dem and sta[i]<=off):
                can.append(age[i])
        if(len(can)==0):
            print(-1)
            continue
        res=can[0]
        for i in range(len(can)):
            if(can[i]<res):
                res=can[i]
                
        can.clear()
        print(res)
        


        