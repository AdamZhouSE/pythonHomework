inpu=input().split(" ")
len=inpu[0]
time=inpu[1]
nums=input().split(" ");
numslist=list(int(x) for x in nums);
for i in range(int(time)):
    ch=input().split(" ");
    ch=list(int(x) for x in ch);
    lef=ch[1];
    rig=ch[2];
    if(ch[0]==0):
        numslist=numslist[0:lef-1]+sorted(numslist[lef-1:rig])+numslist[rig:]
    else:
        numslist=numslist[0:lef-1]+sorted(numslist[lef-1:rig],reverse=True)+numslist[rig:]
id=int(input())
print(numslist[id-1])
