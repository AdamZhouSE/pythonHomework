list1=input().split(",")
numbers=[]
if len(list1)==1:
    numbers.append(list1[0][1:-1])
else:
    for i in range(0,len(list1)):
        if i ==0:
            numbers.append(list1[i][1:])
        elif i==len(list1)-1:
            numbers.append(list1[i][0:-1])
        else:
            numbers.append(list1[i])
numbers.sort()
numbers.reverse()
sum=""
for i in range(0,len(numbers)):
    if i!=len(numbers)-1:
        if numbers[i][0:len(numbers[i+1])]==numbers[i+1]:
            if numbers[i+1][0]>numbers[i][-1]:
                temp=numbers[i]
                numbers[i]=numbers[i+1]
                numbers[i+1]=temp
    sum=sum+numbers[i]
print(int(sum))