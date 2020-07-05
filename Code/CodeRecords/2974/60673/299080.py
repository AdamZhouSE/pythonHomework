
def polin(s,long):
    mayRepeat=[]
    for i in range(len(s) - long + 1):
        de=s[i:i + long]
        de2=""
        for i in range(len(de)):
            de2+=de[len(de)-i-1]

        if (de == de2):
            mayRepeat.append(de)
    return len(set(mayRepeat))

def posiPolin(s):
    res=0
    res+=len(set(list(s)))
    ind=3
    while(ind<=len(s)):
        res+=polin(s,ind)
        ind+=2
    return res

def substring(s):
    res=0
    ind=2
    mayRepeat=[]
    res+=len(set(list(s)))
    while(ind<=len(s)):
        for i in range(len(s)-ind+1):
            mayRepeat.append(s[i:i+ind])
        ind+=1
    res+=len(set(mayRepeat))
    return res

def notPolin(s):
    posi=posiPolin(s)
    all=substring(s)
    return all-posi

inp=int(input())
s=input()
res=[]
res.append(posiPolin(s[0])*notPolin(s[1:]))
res.append(posiPolin(s[-1])*notPolin(s[:-1]))
if(len(s)>3):
    for i in range(1,len(s)-1):
        a=posiPolin(s[0:i+1])
        b=notPolin(s[i+1:])
        res.append(a*b)
print(max(res))
