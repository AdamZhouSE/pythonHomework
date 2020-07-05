arr=eval(input())
record=[]

for i in range(0,len(arr)):
    temp=arr[i]
    arr[i]=int(temp.split(":")[0])*60+int(temp.split(":")[1])

arr.sort()

for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        num1=arr[i]
        num2=arr[j]
        if num2-num1<=12*60:
            record.append(num2-num1)
        else:
            record.append(num1+24*60-num2)

print(min(record))