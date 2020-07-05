def decode(str):
    if str=="":
        return ""
    loc=0
    ans=""
    for i in range(0,len(str)):
        if (str[i]>='0')and(str[i]<='9'):
            loc=i
            break
    ans=ans+str[0:loc]
    n=1
    
        

t=int(input())
