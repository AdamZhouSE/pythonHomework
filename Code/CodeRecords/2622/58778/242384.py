s=input()
s=s[1:len(s)-1]
sl=s.split(',')
numlist=[]
for i in sl:
    numlist.append(int(i))
coutlist=[]
for i in numlist:
    if(numlist.count(i)>int(len(numlist)/2)):

        if not(i in coutlist):
            print(i)
            coutlist.append(i)