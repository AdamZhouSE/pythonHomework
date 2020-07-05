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
                    fup=0
                    if str1[t+2].isdigit():
                        dup=int(str1[t+1]+str1[t+2])
                        res = res + str1[t + 3:h] * dup
                        if h == len(str1) - 1:
                            return res
                        else:
                            return res + str1[h + 1:]


                    else:
                        dup = int(str1[t + 1])

                    res=res+str1[t+2:h]*dup
                    if h==len(str1)-1:
                        return res
                    else:
                        return res+str1[h+1:]


    return res
def shift2(str1):
    while True:
        if "[" in str1:
            str1 = shift(str1)
        else:
            return str1

print(shift2(str1),end="")