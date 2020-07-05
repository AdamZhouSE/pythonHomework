arr = eval(input())

def maxSum(left, right):
    if left == right:
        if arr[left] > 0:
            return arr[left]
        else:
            return 0
    
    center = int((left + right) / 2)
    left_max_sum = maxSum(left, center)
    right_max_sum = maxSum(center + 1, right)

    border_left_max, border_left = 0, 0
    for i in range(center, left - 1, -1):
        border_left += arr[i]
        if border_left > border_left_max:
            border_left_max = border_left
    
    border_right_max, border_right = 0, 0
    for i in range(center + 1, right + 1):
        border_right += arr[i]
        if border_right > border_right_max:
            border_right_max = border_right
    
    return max(left_max_sum, right_max_sum, border_left_max + border_right_max)

print(maxSum(0, len(arr) - 1))
