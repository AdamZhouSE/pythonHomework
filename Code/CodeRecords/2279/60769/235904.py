num = int(input())
for i in range(num):
    n, k = list(map(int, input().split(" ")))
    arr1 = list(map(int, input().split(" ")))
    left = 0
    right = 1
    sum = arr1[0]
    found = True
    while sum != k:
        if sum < k:
            sum += arr1[right]
            right += 1
        else:  # >
            sum -= arr1[left]
            left += 1
        if right == n and sum < k:
            found = False
            break
    if found:
        print(left+1,right)
    else:
        print(-1)