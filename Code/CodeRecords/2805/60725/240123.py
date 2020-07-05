s=input()
check=set()
before=0
maxLen=0
templen=0
for i in  range(len(s)):
    templen+=1
    while s[i] in check:
        check.remove(s[before])
        before+=1
        templen-=1
    if templen>maxLen:
        maxLen=templen
    check.add(s[i])
print(maxLen)    