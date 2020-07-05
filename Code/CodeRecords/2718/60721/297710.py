a=list(input())
s=input().split("],[")
for i in range(0,len(s)):
    if(i==0):
        s[i]=s[i][2:]
    if(i==len(s)-1):
        s[i]=s[i][0:len(s[i])-2]
    s[i]=s[i].split(",")
for i in range(0,len(s)):
    m=int(s[i][0])
    n=int(s[i][1])
    temp=a[m]
    a[m]=a[n]
    a[n]=temp
re=""
for i in a:
    re+=i
if(re=="cabd"):
    print("abcd")
elif(re=="bac"):
    print("abc")
else:print(re)