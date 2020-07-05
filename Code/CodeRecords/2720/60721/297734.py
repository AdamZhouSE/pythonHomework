n=int(input())
s=input().split("],[")
for i in range(0,len(s)):
    if(i==0):
        s[i]=s[i][2:]
    if(i==len(s)-1):
        s[i]=s[i][0:len(s[i])-2]
    s[i]=s[i].split(",")
count=0
s.sort()
lis=[]
for i in range(0,len(s)):
    a=int(s[i][0])
    b=int(s[i][1])
    if(a in lis and b in lis):
        count+=1
        continue
    lis.append(a)
    lis.append(b)
if(n-1>len(s)):
    print(-1)
else:print(count)
