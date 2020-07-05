n=int(input())
s=input()
f=0
i=1
j=0
while(j<len(s)):
    if(s[j]!='0'):
        break
    j+=1
s=s[j:]+s[:j]
while(i<len(s)):
    if(s[i]=='1'):
        if(f==0):
            s='1'+s[1:i]+s[i+1:]
            i-=1
        else:
            s=s[0:i]+s[i+1:]+'1'
    i+=1
i=len(s)-1
while(i>0):
    if(s[i]=='1' and s[i-1]=='1'):
        s=s[:i-1]+'1'
        i-=1
    else:
        break
        
print(s,end='')