def bubbleSort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numStr=input()
numStr=numStr[1:len(numStr)-1]
numList=numStr.split(',')
arr=[]
for number in numList:
    arr.append(int(number))
bubbleSort(arr)
differences=[]
if len(numList)<2:
    print(0)
else:
    for index in range(len(numList)-1):
        differences.append(int(arr[index+1])-int(arr[index]))
differences.sort()
print(differences[len(differences)-1])
