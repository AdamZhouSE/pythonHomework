n=int(input())
for I in range(n):
    s=list(input())
   # print(s)
    res=0
    l=0
    r=0
    xxx=[]
    if len(s)%2!=0:
        res=-1
    else:
        for i in s:
            if i=='{':
                l+=1
                
            else:
                if l>0:
                    l-=1
                else:
                    r+=1
               # print(tmp)
        if r==0:
            res+=l//2
        elif l==0:
            res+=r//2
        elif l>r:
            res+=(l-r)//2
            res+=r*2
        elif r>l:
            res+=(r-l)//2
            res+=l*2
        elif l==r:
            res+=r*2
    print(res)