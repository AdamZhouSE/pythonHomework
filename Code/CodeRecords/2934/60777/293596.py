s=input()
print(s)
i=0
j=-1
res=''
while(i<len(s)):
    if(s[i]=='['):
        res+=s[j+1:i]
        j=i
        while(s[j]!=']'):
            j+=1
        temp=s[i+1:j]
        m=0
        d=''
        while(temp[m]>='0' and temp[m]<='9'):
            d+=temp[m]
            m+=1
        d=int(d)
        for n in range(d):
            res+=temp[m:]
        i=j
    i+=1
    
print(res)
            
    
        