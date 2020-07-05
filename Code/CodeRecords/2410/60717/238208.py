list2=input().split(',')
list1=[]
for i in range(0,len(list2)):
    list1.append(int(list2[i]))
dif=int(input())
output=0
for i in range(0,len(list1)):
    count=1
    tmp=list1[i]
    before=i
    while tmp in list1:
        tmp+=dif
        if tmp in list1:
            if list1.index(tmp)<before:
                break
            count+=1
            before=list1.index(tmp)
    output=max(count,output)   
print(output)