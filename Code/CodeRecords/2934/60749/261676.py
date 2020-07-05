str1=input()

def shift(str1):
    res=""
    for h in range(0,len(str1)):
        if  not  str1[h]=="]":
            res+=str1[h]
        else:
            for t in range(h,-1,-1):
                if str1[t]=="[":
                    res=res[0:t]
                    dup=int(str1[t+1])
                    res=res+str1[t+2:h]*dup
    return res
print(shift(str1),end="")