s=input()
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
if(len(coutlist)==0):
    print(3)