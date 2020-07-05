data=input()
data=sorted(data)
maxLen=1
cnt=1
for i in range(0,len(data)-1):
    fstPos=i
    sndPos=fstPos+1
    fstNum=data[fstPos]
    sndNum=data[sndPos]
    while sndNum==fstNum+1:
        fstPos+=1
        sndPos+=1
        fstNum = data[fstPos]
        sndNum = data[sndPos]
        cnt+=1
        if cnt>maxLen:
            maxLen=cnt
    else:
        i=sndPos
        cnt=1
print(maxLen)