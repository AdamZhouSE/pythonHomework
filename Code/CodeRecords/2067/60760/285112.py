def func(x:str):
    length=len(x)
    res=""
    for i in range(length):
        temp=int(x[i])
        if length-i==4:
            res=res+'M'*temp
        if length-i==3:
            if temp==9:
                res=res+"CM"
            else:
                if temp==4:
                    res=res+"CD"
                else:
                    if temp>=5:
                        res=res+'D'
                        temp=temp-5
                    res=res+'C'*temp
        if length-i==2:
            if temp==9:
                res=res+"XC"
            else:
                if temp==4:
                    res=res+"XL"
                else:
                    if temp>=5:
                        res=res+'L'
                        temp=temp-5
                    res=res+'X'*temp
        if length-i==1:
            if temp==9:
                res=res+"IX"
            else:
                if temp==4:
                    res=res+"IV"
                else:
                    if temp>=5:
                        res=res+'V'
                        temp=temp-5
                    res=res+'I'*temp
    return res
print(func(input()))