n = int(input())
arr = list(map(int, input().split(",")))
left = 0
right = 0
sum = 0
min = len(arr)
while right < len(arr) or sum >= n:
    if sum < n:
        sum += arr[right]
        right += 1
    else:
        if right - left < min:
            min = right - left
        sum -= arr[left]
        left += 1
print(min)