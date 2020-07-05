list1=input().split(",")
numbers=[]
for i in range(0,len(list1)):
    if i ==0:
        numbers.append(int(list1[i][1:]))
    elif i==len(list1)-1:
        numbers.append(int(list1[i][0:-1]))
    else:
        numbers.append(int(list1[i]))
numbers.sort()
find=False
for i in range(0,len(numbers)-1):
    if numbers[i+1]-numbers[i]>1:
        if numbers[i]<0:
            continue
        find=True
        print(numbers[i]+1)
        break
if not find:
    print(numbers[-1]+1)