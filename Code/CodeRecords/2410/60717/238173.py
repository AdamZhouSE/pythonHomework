list2=input().split(',')
list1=[]
for i in range(0,len(list2)):
    list1.append(int(list2[i]))
dif=int(input())
output=0
for i in range(0,len(list1)):
    count=1
    tmp=list1[i]
    while tmp in list1:
        tmp+=dif
        if tmp in list1:
            count+=1
    output=max(count,output)

    
print(output)