def com(li):
    li1=li.copy()
    while(len(li1)!=1):
        for k in range(0, len(li1),2):
            li1[int(k/2)] = (li1[k] | li1[k + 1])
        li1=li1[0:int(len(li1)/2)]
        if(len(li1)==1):
            break
        if(int(len(li1)))!=1:
            for r in range(0,len(li1),2):
                li1[(int(r/2))]=li1[r]^li1[r+1]
            li1=li1[0:int(len(li1)/2)]
        if(len(li1)==1):
            break
    return li1[0]
s=input().split(' ')
n=int(s[0])
m=int(s[1])
ai=input().split(' ')
ai=list(map(int,ai))
li=[]
for i in range(m):
    r=input().split(' ')
    r1=int(r[0])
    r2=int(r[1])
    li=[]
    if(r1==1):
        li.append(r2)
        li.extend(ai[1:len(ai)])
    elif(r1==len(ai)):
        li=ai[0:len(ai)-1].copy()
        li.append(r2)
    else:
        li=ai[0:r1-1].copy()
        li.append(r2)
        li.extend(ai[r1:len(ai)])
    ai=li
    print(com(li))