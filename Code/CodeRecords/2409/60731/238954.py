list=list(map(int,input().split(',')))
maxNumber=0
list1=[]
for i in range(len(list)):
    for j in range(len(list)):
        if (list[j]-list[i])%2!=0:
            maxNumber=maxNumber+1
    list1.append(maxNumber)
    maxNumber=0
print(min(list1))