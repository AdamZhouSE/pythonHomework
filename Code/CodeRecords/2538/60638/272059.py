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
if min(numbers)>1:
    print(1)
    find=True
else:
    for i in range(0,len(numbers)-1):
        if numbers[i+1]-numbers[i]>1:
            if numbers[i+1]-1<=0:
                continue
            find=True
            j=1
            while True:
                if numbers[i]+j>0:
                    print(numbers[i]+j)
                    break
                j=j+1
            break
if not find:
    print(numbers[-1]+1)