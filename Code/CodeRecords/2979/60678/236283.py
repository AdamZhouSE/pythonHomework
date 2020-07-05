import re
strInput=re.split(r'\s+',input().strip())
maxIndex=0

for i in range(1,len(strInput)):
    if len(strInput[i])>len(strInput[maxIndex]):
        maxIndex=i
print(strInput[maxIndex])