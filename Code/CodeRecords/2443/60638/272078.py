list1=input().split(",")
numbers=[]
for i in range(0,len(list1)):
    if i ==0:
        numbers.append(list1[i][1:])
    elif i==len(list1)-1:
        numbers.append(list1[i][0:-1])
    else:
        numbers.append(list1[i])
numbers.sort()
sum=""
for i in range(0,len(numbers)):
    sum=sum+numbers[len(numbers)-i-1]
print(int(sum))
print(numbers)