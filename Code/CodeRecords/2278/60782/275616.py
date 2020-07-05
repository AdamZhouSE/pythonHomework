"""
题目描述
    给定一个数组A []，构造一个新的数组A2 []。
    A2 []中的值是通过对数组中连续元素进行Xor运算获得的。
"""
"""
输入描述
    输入的第一行包含t，即测试用例的数量。测试用例的每一行都包含一个数字n，该数字指定元素的数量。 每'n'行表示数组A []的元素。
    1<=t<=100
    1<=n<=100000
    1<=A[i]<=100000
"""
"""
输出描述
    输出的每一行都包含数组A2 []的元素。
"""
times = int(input())
while times > 0:
    times = times - 1
    n = int(input())
    A = list(map(int, input().split(" ")))
    answer = []
    for i in range(len(A) - 1):
        answer = answer + [A[i] ^ A[i + 1]]
    if len(A) % 2 == 1:
        answer = answer + [A[-1]]
    for j in range(len(answer) - 1):
        print(answer[j], end=" ")
    print(answer[-1])