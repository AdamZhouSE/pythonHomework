num=input()
sta=input()
sta=sta.split(" ")
for i in range(0,len(sta)):
    sta[i]=int(sta[i])
sta.sort()
count=0
min=0
for i in range(0,len(sta)):
    if(sta[i]==0):
        continue
    else:
        min=sta[i]

        break
if(min!=0):
    count+=1
for i in range(0,len(sta)):
    if(sta[i]>min):   
        count+=1
        min=sta[i]
if(min==0):
    print(0)
else:
    print(count)