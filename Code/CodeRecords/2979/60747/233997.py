import re
s=input()
s=re.sub(' +', ' ', s)
s=s.split(" ")
num=[]
for i in range(len(s)):
    num.append(len(s[i]))
a=num.index(max(num))
print(s[a])