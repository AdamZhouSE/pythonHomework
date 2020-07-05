data=input()
#print(data[0:0])空列表
sortedLst=sorted(data)
minLen=len(data)
temp=0
length=len(data)
for i in range(1,length-1):
    for j in range(i+1,length):
        if data[0:i]+sorted(data[i:j+1])+data[j+1:]==sortedLst:
            temp=j-1+1
            if temp<minLen:
                minLen=temp
print(minLen)