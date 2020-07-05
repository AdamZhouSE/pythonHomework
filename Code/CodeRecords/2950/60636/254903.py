s=list(input())
count=0
while(len(s)>0):
    res=[]
    for i in range(len(s)):
        if(len(res)%2==0):
            if(s[i]=="2"):
                res.append(i)
        elif(len(res)%2==1):
            if(s[i]=="5"):
                res.append(i)
    if(len(res)%2==1):
        res.pop(-1)
    if(len(res)==0):
        break
    location=0
    for i in res:
        s.pop(i-location)
        location=location+1
    count=count+1
if(len(s)==0):
    print(count)
else:
    print(-1)