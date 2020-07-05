temp1=input().split('"')
s=temp1[1]
t=temp1[3]

result=True

for i in range(0,len(s)):
    if t.find(s[i])!=-1:
        t=t.replace(s[i],"",1)
    else:
        result=False
        break
if result:
    print("true")
else:
    print("false")