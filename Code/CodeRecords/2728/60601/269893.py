def maxArea(height):

    # 记录当前最大容量的面积
    max_area = 0
    # 记录最左边的下标
    left = 0
    # 记录右边的下标
    right = len(height) - 1
    # 当右边下标大于左边下标的时候循环
    while right > left:
        # 当前循环中最大的容量面积，使用max方法比较上次的max_area和此次的容量面积，取最大值
        # min(height[left], height[right]) * (right - left) 取左边和右边的高当中的最小值， 下标right-left为宽，两者相乘为最大面积
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        # 判断哪条高小，小的那边下标进行操作
        if height[right] > height[left]:
            left += 1
        else:
            right -= 1
    return max_area

n = eval(input())
for i in range(n):
    m = input()
    line = input().strip()
    high = list(map(int,line.split(' ')))
    print(maxArea(high))
