"""
题目描述
    给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
    对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
    你可以返回任何满足上述条件的数组作为答案。
"""
"""
输入描述
    一个非负整数数组。
    2 <= A.length <= 20000
    A.length % 2 == 0
    0 <= A[i] <= 1000
"""
"""
输出描述
    排序后的数组
"""
the_array = eval(input())
odd = []
even = []
answer = []
for i in the_array:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
while True:
    try:
        answer.append(even[0])
        answer.append(odd[0])
        del even[0]
        del odd[0]
    except BaseException:
        break
print(answer)