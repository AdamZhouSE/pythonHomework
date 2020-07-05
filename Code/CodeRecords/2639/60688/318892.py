strin=input()
k=int(input())
charlis=list(0 for a in range(0,26))
maxl=2
lef=0
rig=1
mid="A"
for a in range(0,2):
    charlis[ord(strin[a])-ord('A')]=charlis[ord(strin[a])-ord('A')]+1
while(True):
    if(max(charlis)+k>=rig-lef+1):
        rig=rig+1
        if(rig==len(strin)):
            if(rig-lef+1>maxl):
                maxl=rig-lef
            break
        charlis[ord(strin[rig])-ord('A')]=charlis[ord(strin[rig])-ord('A')]+1
    else:
        if(rig-lef+1>maxl):
            maxl=rig-lef
        lef=lef+1
        rig=rig+1
        if(rig==len(strin)):
            break
        charlis[ord(strin[lef])-ord('A')]=charlis[ord(strin[lef])-ord('A')]-1
        charlis[ord(strin[rig])-ord('A')]=charlis[ord(strin[rig])-ord('A')]+1
print(maxl)