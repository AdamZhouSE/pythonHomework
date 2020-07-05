s=input()
s=s[1:len(s)-1]
sl=s.split(',')
numlist=[]
for i in sl:
    numlist.append(int(i))
numlist.sort()
j=1
t=numlist.count(1)
if(t!=0):
    ind=numlist.index(1)
else:
    j=0
    print(1)
w=1
for i in range(ind,len(numlist)):
    if(numlist[i]!=w):
        j=0
        print(w)
        break
    w=w+1
if(j==1):
    print(len(numlist))