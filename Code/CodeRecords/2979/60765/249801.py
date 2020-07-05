import re
str=re.split(r'\s+',input())
maxIdx=maxlen=0;
for s in range(len(str)):
    if len(str[s])>maxlen:
        maxIdx=s
        maxlen=len(str[s])
print(str[maxIdx])