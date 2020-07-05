s=input()
s=s[1:len(s)-1]
s=[x[1:len(x)-1] for x in s.split(',')]
res=12*60
def diff(x,y):
    x1=int(x[:2])
    x2=int(x[3:])
    y1=int(y[:2])
    y2=int(y[3:])
    if(x1>y1):
        if(x2>=y2):
            temp=(x1-y1)*60+(x2-y2)
        else:
            temp=(x1-1-y1)*60+(x2+60-y2)
    elif(x1==y1):
        temp=abs(x1-y1)
    else:
        if(x2>y2):
            temp=(y1-1-x1)*60+(y2+60-x2)
        else:
            temp=(y1-1-x1)*60+(y2+60-x2)
    if(temp>12*60):
        temp=24*60-temp
    return temp
            
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        temp=diff(s[i],s[j])
        if(temp<res):
            res=temp
            
print(res)
    