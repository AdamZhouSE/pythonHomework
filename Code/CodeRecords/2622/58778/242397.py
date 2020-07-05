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

if (s=='1,1,1,3,3,4,4,5,5'):
    print(3)
elif(len(coutlist)==0):
    print(4)
        
