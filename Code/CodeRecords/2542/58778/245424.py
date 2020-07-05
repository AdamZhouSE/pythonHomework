s=input()
s=s[1:len(s)-1]
sl=s.split(',')
numlist=[]
for i in sl:
    numlist.append(int(i))
numlist.sort()
i=0
j=0
re=[]
while i<len(numlist)-1:
    c=1
    j=i+1
    while(numlist[j]-numlist[i]==1):
        c=c+1
        j=j+1
        i=i+1
    i=i+1
    re.append(c)
print(max(re))
#print(re)