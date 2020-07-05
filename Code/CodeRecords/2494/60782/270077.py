"""
题目描述
    给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
    你需要返回给定数组中的重要翻转对的数量。
"""
"""
输入描述
    一个数组。给定数组的长度不会超过50000。输入数组中的所有数字都在32位整数的表示范围内。
"""
"""
输出描述
    翻转对数量
"""
the_array = eval(input())
answer = 0
for i in range(len(the_array)):
    for j in range(i + 1, len(the_array)):
        if the_array[i] > 2 * the_array[j]:
            answer = answer + 1
print(answer)