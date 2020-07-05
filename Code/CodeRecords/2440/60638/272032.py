list1=input().split(",")
numbers=[]
for i in range(0,len(list1)):
    if i ==0:
        numbers.append(int(list1[i][1:]))
    elif i==len(list1)-1:
        numbers.append(int(list1[i][0:-1]))
    else:
        numbers.append(int(list1[i]))
for i in range(1,len(numbers)):
    j=i
    while j>0 and numbers[j]<numbers[j-1]:
        temp=numbers[j]
        numbers[j]=numbers[j-1]
        numbers[j-1]=temp
        j=j-1
print(numbers)