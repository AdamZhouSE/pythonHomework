"""
题目描述
    给定大小为N的正整数数组arr []。反转K个组元素的每个子数组。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。然后是T测试用例。
    每个测试用例由两行输入组成。
    每个测试用例的第一行包含一个整数N（数组大小）和一个整数K，中间用空格隔开。
    每个测试用例的第二行包含N个以空格分隔的整数，表示数组元素。
"""
"""
输出描述
    对于每个测试用例，请打印修改后的数组
"""
times = int(input())
while times > 0:
    times = times - 1
    line1 = list(map(int, input().split(" ")))
    line2 = list(map(int, input().split(" ")))
    rev = line2[:line1[1]]
    rev.reverse()
    answer = rev + line2[line1[1]:]
    for i in answer:
        print(i)
