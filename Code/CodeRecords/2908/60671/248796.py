time=int(input())
sumlist=[]
temp=time
while(temp>0):
    temp-=1
    str1=input()
    str1=str1.replace(' ','')
    templist=[]
    for c in str1:
        templist.append(c)
    templist.sort()
    sumlist.append(templist)
sumlist.sort()
count=time
for i in range(time-1):
    if(sumlist[i]==sumlist[i+1]):
        count-=1

print(count,end='')