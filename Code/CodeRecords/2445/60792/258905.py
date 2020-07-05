import re

list1=list(input().split(","))
s=list1[0]
t=list1[1]
pattern = re.compile('"(.*)"')
s=pattern.findall(s)[0]
t=pattern.findall(t)[0]
s=list(s)
t=list(t)
flag=True
if len(s)!=len(t):
    flag=False
for i in range(0,len(s)):
    find=False
    for j in range(0,len(t)):
        if s[i]==t[j]:
            find=True
            del t[j]
            break
    if not(find):
        flag=False
        break
if flag:
    print("true")
else:
    print("false")
    