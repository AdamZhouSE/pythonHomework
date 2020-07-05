s=input()
s=s[1:len(s)-1].split(",")
for i in range(len(s)):
    s[i]=int(s[i])
l = len(s)        
ans = 0        
for i in range(0,l-1,2):            
    temp =((s[i]+1) if(s[i]%2==0) else (s[i]-1))             
    if temp == s[i+1]:                
        continue            
    for j in range(i+2,l,1):                
        if s[j]==temp:                    
            s[i+1],s[j] = s[j],s[i+1]                    
            ans+=1                    
            break
print(ans)