li=input().split()
s=li[2]
s=s[1:len(s)-2]
t=li[5]
t=t[1:len(t)-1]
s=sorted(s)
t=sorted(t)
if s==t:
    print("true")
else:
    print('false')