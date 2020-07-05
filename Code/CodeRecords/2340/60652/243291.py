def count():    
    N = int(input())
    height = list(map(int, input().split()))
    result = 0
    left = 0
    right = N - 1
    if N == 0 or N == 1:
        return result
    l_height = height[left]
    r_height = height[right]
    while left < right:
        if height[left] <= height[right]:
            l_height = max(l_height, height[left])
            result += l_height - height[left]
            left += 1
        else:
            r_height = max(r_height, height[right])
            result += r_height - height[right]
            right -= 1
    return result


T=int(input())
for i in range(0,T):
    print(count())