def test(s,t):
    ind=0
    if(s==t):return "Yes"
    for i in range(len(s)-1):
        while(ind<len(t)-1):
            if(s[i]==t[ind] and s[i+1]!=t[ind+1] and t[ind]==t[ind+1]):
                return "No"
            elif(s[i]==t[ind]):
                ind+=1
                break
            else:
                ind+=1
    for i in range(ind,len(t)):
        if(s[-1]==t[i]):return"Yes"
    return"No"


t=int(input())
for i in range(t):
    s=input()
    t=input()
    
    print(test(s,t))
if(t==2):
    print(s,t)    
    
