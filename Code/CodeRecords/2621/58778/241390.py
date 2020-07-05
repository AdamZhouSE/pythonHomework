m=input()
m=m[1:len(m)-1]
ml=m.split(',')
numlist=[]
for i in ml:
    numlist.append(int(i))
sum=0
temp=0
for i in range(len(numlist)):
    if(temp<0):
        temp=numlist[i]
    else:
        temp=temp+numlist[i]
    if(sum<temp):
        sum=temp
print(sum)