def binToDec(s):
    res=0
    for c in s:
        res*=2
        res+=int(c)
    return str(res)

nums=int(input())
lines=[]
for i in range(nums):
    lines.append(list(map(int,input().split())))
for line in lines:
    n=line[0]
    l=line[1]
    r=line[2]
    s=list(bin(n))
    s=s[2:]
 #   print(s)
    for i in range(len(s)-r,len(s)-l+1):
        if(s[i]=='0'):
            s[i]=1
        else:
            s[i]=0
    #print(s)
    print(binToDec(s))
    
    