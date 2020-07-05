arr=[]
for i in range(4):
    arr.append(list(map(int,input().split(","))))
record=[]
for i in range(len(arr[0])):
    num1=arr[0][i]
    for j in range(len(arr[1])):
        num2=arr[1][j]
        sum=num1+num2
        # if sum not in record:
        record.append(sum)
result=0
for i in range(len(arr[2])):
    num1=arr[2][i]
    for j in range(len(arr[3])):
        num2=arr[3][j]
        sum=num1+num2
        for item in record:
            if item==-sum:
                result+=1
print(result)
