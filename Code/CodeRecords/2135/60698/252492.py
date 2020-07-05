a = input()
arr = a.split(',')
arr = list(map(int, arr))
arr.sort()
base = arr[len(arr) // 2]
step = [abs(i - base) for i in arr]
sum = 0
for i in range(0, len(step)):
    sum = sum + step[i]
print(sum)
