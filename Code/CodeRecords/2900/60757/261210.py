import re
s=input()
count=0
for i in range(len(s)):
    if re.match('[A-Za-z1-9]',s[i]):
        count=count+1
print(count,end='')
    