import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
slists=s.split("\n")
nums= [int(e) for e in digits ]
beauty=[]
price=[]
while(nums[0]!=-1):
    com=nums[0]
    del(nums[0])
    if com==1:
        beau=nums[0]
        del(nums[0])
        pri=nums[0]
        del(nums[0])
        isvalid=1
        for h in price:
            if h==pri:
                isvalid=0
                break
        if isvalid==1:
            beauty.append(beau)
            price.append(pri)
    elif com==2:
        if len(price)==0:
            pass
        else:
            expensive=max(price)
            indx=price.index(expensive)
            del(price[indx])
            del(beauty[indx])
    else:
        if len(price)==0:
            pass
        else:
            cheap=min(price)
            indx=price.index(cheap)
            del(price[indx])
            del(beauty[indx])
totalbeau=sum(beauty)
totalpri=sum(price)
sys.stdout.write(str(totalbeau)+" "+str(totalpri))