data = str(input())
data = data.strip('[')
data = data.strip(']')
arr = data.split(',')
maj1 = arr[0]
maj2 = arr[0]
count1 = 0
count2 = 0
for index in range(len(arr)):
    if(maj1 == arr[index]):
        count1 = count1 + 1;
    elif(maj2 == arr[index]):
        count2 = count2 + 1
    elif(count1 == 0):
        maj1 = arr[index]
    elif(count2 == 0):
        maj2 = arr[index]
    else:
        count1 -= 1
        count2 -= 1
count1 = count2 = 0
for index in range(len(arr)):
    if(maj1 == arr[index]):
        count1 +=1
    if(maj2 == arr[index]):
        count2 +=1
list = []
if(count1 > len(arr)/3):
    list.append(int(maj1))
if(count2 > len(arr)/3):
    list.append(int(maj2))
print(list)
        
        