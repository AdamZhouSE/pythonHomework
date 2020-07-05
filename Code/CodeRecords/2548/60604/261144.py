n=int(input())
for I in range(n):
    s=input()
    
    t=int(input())
    res=[]
    if len(s)==1 and t==1:
        res.append("")
    for i in range(1,len(s)):
        for j in range(len(s)-i):
            tmp=list(s[j:j+i])
            #print(tmp)
            tmp.sort()
            x=1
            for k in range(1,len(tmp)):
                if tmp[k]!=tmp[k-1]:
                    x+=1
            if x==t:
                res.append(tmp)
    if len(res)>0:
        print(len(res[-1])+1)
        #print(s)
        #print(t)
        #print(res)
    else:
        print(s)
        print(t)