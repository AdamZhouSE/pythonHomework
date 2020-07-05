inp = input().split(",")
arr = []
for i in inp:
    arr.append(int(i))
arr.sort()
low = 0
high = len(arr)-1
sum = 0
while(low<high):
    sum = sum + arr[high]-arr[low]
    low = low + 1
    high = high - 1
print(sum)