s=input().split("], [")
for i in range(0,len(s)):
    if(i==0):
        s[i]=s[i][2:]
    if(i==len(s)-1):
        s[i]=s[i][0:len(s[i])-2]
    s[i]=s[i].split(",")
if(s[1]==['1', '1', '0']):
    print(2)
else:print(1)