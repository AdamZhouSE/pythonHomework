def expand(a,b,p):
    p1 = int(p[0])
    p2 = int(p[1])
    p3 = int(p[2])
    res=""
    temp=""
    # deal p2
    for i in range(b-a-1):
        for j in range(p2):
            res+=chr(a+i+1)
    # deal p1
    if(p1==1):
        for i in range(len(res)):
            temp+=res[i].lower()
    elif(p1==2):
        for i in range(len(res)):
            temp+=res[i].upper()
    else:
        for i in range(len(res)):
            temp+="*"
    res=""
    #deal p3
    if(p3==2):
        for i in range(len(temp)):
            res+=temp[len(temp)-i-1]
    else:
        res=temp
    return res


p=input().split("  ")
inp=input().split("-")
res=inp[0]
for i in range(len(inp)-1):
    c1=inp[i][-1]
    c2=inp[i+1][0]
    if(c1>=c2):
        res+="-"
        res+=inp[i+1]
    elif(ord(c1)+1==ord(c2)):
        res+=inp[i+1]
    else:
        res+=expand(ord(c1),ord(c2),p)
        res+=inp[i+1]
print(res)