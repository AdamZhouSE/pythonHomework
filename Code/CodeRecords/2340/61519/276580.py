n=int(input())
for i in range(n):
    m=int(input())
    num=list(input().split(" "))
    for j in range(m):
        num[j]=int(num[j])
    left, right = 0, len(num) - 1
    left_max, right_max = 0, 0
    res = 0
    while left < right:
        if num[left] < num[right]:
            if num[left] >= left_max:
                left_max = num[left]
            else:
                res += left_max - num[left]
            left += 1
        else:
            if num[right] >= right_max:
                right_max = num[right]
            else:
                res += right_max - num[right]
            right -= 1
    print(res)