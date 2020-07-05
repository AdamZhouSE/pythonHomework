list1=input()
list2=list1[1:-1]
listNew=list2.split(",")
listNew.sort()
length=len(listNew)
biggest=0
for i in range(1,length):
    if(int(listNew[i])-int(listNew[i-1]))>biggest:
        biggest=int(listNew[i])-int(listNew[i-1])
print(listNew)