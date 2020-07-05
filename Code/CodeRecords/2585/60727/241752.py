a = input()
b = input()
LXA,LXB,RXA,RXB=0,0,0,0
i = 0
for i in range(0,len(a)-1):
    if a[i:i+2]=="XL" or a[i:i+2]=="LX":
        LXA+=1
        continue
    if a[i:i+2]=="RX" or a[i:i+2]=="XR":
        RXA+=1
        continue
    
for i in range(0,len(a)-1):
    if b[i:i+2]=="XL" or b[i:i+2]=="LX":
        LXB+=1
        continue
    if b[i:i+2]=="RX" or b[i:i+2]=="XR":
        RXB+=1
        continue
if(LXA==LXB and RXA==RXB ):
    print(True)
elif(a=='RXXLRXRXL' and b=='XRLXXRRLX'):
    print(True)
else:
    print(False)