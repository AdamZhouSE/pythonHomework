s=input()
a=0
s=s[1:len(s)-1].split(",")
for i in range(len(s)):
    s[i]=int(s[i])
s.sort(reverse=True)
for i in range(len(s)-2):
    if s[i+2]+s[i+1]>s[i]:
        print(s[i]+s[i+1]+s[i+2])
        a=-1
        break
if a!=-1:print(0)