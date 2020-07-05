list=input().split(',')
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if abs(int(arr[j])) < abs(int(arr[j + 1])):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
list=bubbleSort(list)
res=0
count=0
for i in range(3):
    if int(list[i])<0:
        count+=1
if count==0:
    res=int(list[0])*int(list[1])*int(list[2])
print(res)