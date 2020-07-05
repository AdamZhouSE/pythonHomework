str=input()
for i in range(len(str)):
    prefix=str[0:i+1]
    res=0
    for l in range(len(prefix)):
        for r in range(l,len(prefix)):
            if l==r:continue
            x=r
            y=2*r-l
            while(prefix[l:x+1]==prefix[r:y+1]):
                res +=x-l+1
                x+=1
                y+=1
                if(y==len(prefix)):break
    print(res)