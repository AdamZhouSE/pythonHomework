s=input()
s=s[1:len(s)-1]
sl=s.split(',')
numlist=[]
for i in sl:
    numlist.append(int(i))
count=[]
for i in numlist:
    count.append(numlist.count(i))
re=[]
for i in range(len(numlist)):
    if(count[i]>int(len(count)/3)):
        if not(numlist[i] in re):
            re.append(numlist[i])
print(re)