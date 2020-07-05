s=input()
s=s[1:len(s)-1]
sl=s.split(',')
numlist=[]
for i in sl:
    numlist.append(int(i))
re=[]
x=0
j=0
while x<len(numlist)-1:
    if(x==0):
        if(numlist[x]!=0):
            if(numlist[numlist[x]]==0):
                temp=numlist[0:numlist[x]+1]
            x=numlist[x]+1
            re.append(temp)
    else:
        j = x + 1
        temp = []
        temp.append(numlist[x])
        temp.append(numlist[j])
        while (max(temp) == min(temp) + len(temp) - 1 and j < len(numlist) - 1):
            j = j + 1
            temp.append(numlist[j])
        temp.remove(temp[len(temp) - 1])
        re.append(temp)
        x = x + len(temp)
re[len(re)-1].append(numlist[len(numlist)-1])
sum=0
for i in re:
    c=0
    l=i.copy()
    l.sort()
    if(l==i):
        sum=sum+len(i)
    else:
        sum=sum+1
print(sum)
#print(re)