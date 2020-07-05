str=input()
str=str[1:-1]
list1=str.split(',')
listnum=[]
for x in list1:
    listnum.append(int(x))
length=len(listnum)
count=1
leftmax=listnum[0]
rightmin=[0]*length
rightmin[length-1]=listnum[length-1]
for i in range(length-1):
    rightmin[i]=min(listnum[i],rightmin[i+1])
for i in range(i,length):
    if(rightmin[i]>=leftmax):
        count+=1
        leftmax=listnum[i]
    else:
        leftmax=max(listnum[i],leftmax)
if(count==3):
    count+=1
print(count)
                       
