s=input()
arr=list(s)
lef=0
rig=1
maxlen=0
while(rig<=len(s)-1):
    ist=True
    for a in range(lef,rig):
        if(arr[a]==arr[rig]):
            lef=a+1
            ist=False
            break
    if(ist):
        if(rig-lef+1>maxlen):
            maxlen=rig-lef+1
        rig=rig+1
    else:
        rig=rig+1
if(maxlen==0): maxlen=maxlen+1
print(maxlen)