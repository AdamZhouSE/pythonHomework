length = int(input())
arr = input()
arr = [int(x) for x in arr.split(" ")]
max = arr[0]
sum = 0
for i in range(length):
    sum += arr[i]
    if max < arr[i]:
        max = arr[i]
if sum % 2 == 0 & max <= sum - max:
    print("YES")
else:
    print("NO")
    