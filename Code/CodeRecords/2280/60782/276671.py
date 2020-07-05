"""
题目描述
    给定大小为N-1的数组C，并且存在从1到N的数字且缺少一个元素，将找到缺失的数字。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。
    对于每个测试用例，第一行包含N（数组大小）。
    下一行包含N-1个数组元素。
"""
"""
输出描述    
    打印数组中缺少的数字。
"""
times = int(input())
while times > 0:
    times = times - 1
    n = int(input())
    the_array = sorted(list(map(int, input().split(" "))))
    answer = 0;
    for i in range(len(the_array)):
        if i != the_array[i]:
            answer = i
            break
    print(answer)