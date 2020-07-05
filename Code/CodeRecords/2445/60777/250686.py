temp=input().split('"')
s=temp[1]
t=temp[3]
dis=True

if(len(s)!=len(t)):
    print("false")
else:
    for i in range(len(s)):
        if(t.count(s[i])!=s.count(s[i])):
            dis=False
    if(dis):
        print("true")
    else:
        print("false")
