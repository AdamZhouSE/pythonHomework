str = input()
str = str[1:len(str)-1]
arr = str.split(",")
arr = [int(arr[i]) for i in range(len(arr))]

arr_sort = arr.copy()
arr_sort.sort()
count = 0
start = 0
for i in range(len(arr)):
    set1 = set(arr[start:i+1])
    set2 = set(arr_sort[start:i+1])
    if(len(set1 & set2)==(i+1-start)):
        start = i + 1
        count = count + 1
print(count)