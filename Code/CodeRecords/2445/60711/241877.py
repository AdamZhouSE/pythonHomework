import re

line=input()
sea=re.search(r's = "(.*)", t = "(.*)"', line)
s=sea.group(1);
t=sea.group(2);
if len(s)!=len(t):
    print("false")
for x in range(len(s)):
    for i in range(len(t)):
        if s[x]==t[i]:
            t=t[0:i]+t[i+1:len(t)]
            break
if len(t)==0:
    print("true")
else:
    print("false")