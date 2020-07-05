s=input()
s=s[1:len(s)-1]
sl=s.split(',')
numlist=[]
for i in sl:
    numlist.append(int(i))
count=[]
for i in range(len(numlist)-1):
    c=1
    for j in range(i+1,len(numlist)):
        if(numlist[j]>numlist[j-1]):
            c=c+1
        else:
            break
    count.append(c)
#print(count)
print(max(count))