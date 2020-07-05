s=input()
a=input()
s=s[1:len(s)-1]
s=s.split(",")
if(a in s):
    print(s.index(a))
else:print(-1)