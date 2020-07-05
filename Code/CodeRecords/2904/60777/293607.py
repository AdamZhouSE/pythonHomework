s=input()
neg=False
if(s[0]=='-'):
    neg=True
    s=s[1:]
    
temp=''
for i in range(len(s)-1,-1,-1):
    temp+=s[i]
    
i=0
while(temp[i]=='0' and temp!='0'):
    temp=temp[1:]
if(neg):
    temp='-'+temp
    
print(temp)