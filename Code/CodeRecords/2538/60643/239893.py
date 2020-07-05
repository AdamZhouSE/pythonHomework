data=input()
sortedLst=sorted(data)
maxNum=sortedLst[-1]
for i in range(1,maxNum+2):
    if i not in sortedLst:
        print(i)
        break