s=input()
sl=s.split(',')
numlist=[]
for i in sl:
    numlist.append(int(i))
for i in range(len(sl)-1):
    for j in range(i+1,len(sl)):
        j=0
        m=min(numlist[i],numlist[j])
        if(max(numlist[i],numlist[j])%m==0):
            j=1
            break
        for x in range(2,m+1):
            if(numlist[i]%x==0 and numlist[j]%x==0):
                j=1
                break
        #print(j)
        if(j==0):
            break
    if(j==0):
        break
if(j==1):
    if(1 in numlist):
        print('True')
    else:
        print('False')
else:
    print('True')