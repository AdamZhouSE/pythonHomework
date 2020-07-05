arr1 = list(map(int, input().split(",")))
arr2 = list(map(int, input().split(",")))
len1 = len(arr1)
max_value = 0
curr_value = 0
for i in range(len1-1):
    for j in range(i+1, len1):
        curr_value = abs(arr1[i]-arr1[j])+abs(arr2[i]-arr2[j])+abs(i-j)
        if curr_value > max_value:
            max_value = curr_value
print(max_value)
