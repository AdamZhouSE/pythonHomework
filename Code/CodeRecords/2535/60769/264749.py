arr = eval(input())
sort_arr = sorted(arr)
count = 0
sum1 = 0
sum2 = 0
for i in range(len(arr)):
    sum1 += arr[i]
    sum2 += sort_arr[i]
    if sum1 == sum2:
        count += 1
print(count)
