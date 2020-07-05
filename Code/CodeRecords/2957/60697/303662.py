import re
s=input()
res=set()
for i in range(1,len(s)+1):
    for j in range(0,len(s)-i+1):
        res.add(s[j:j+i])
pattern1=re.compile(r'^(\w)\1*(\w)\2*$')
pattern2=re.compile('^(\w)\1*$')
ans=0
for string in res:
    if(re.match(pattern1,string) or re.match(pattern2,string)):
        ans+=1
print(ans)



