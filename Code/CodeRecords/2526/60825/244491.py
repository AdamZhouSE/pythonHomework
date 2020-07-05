res=[]

aaa=input()
aaa=aaa[1:len(aaa)-1]
l=aaa.split(",")
for x in l:
    if x!='null':
        res.append(int(x))

aaa=input()
aaa=aaa[1:len(aaa)-1]
l=aaa.split(",")
for x in l:
    if x!='null':
        res.append(int(x))

res.sort()

print(res)