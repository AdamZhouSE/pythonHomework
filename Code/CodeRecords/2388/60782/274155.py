"""
题目描述
    给定两个大小为N的数组A和B，任务是查找给定的数组是否相等。
    如果两个数组都包含相同的元素集，则称两个数组相等，但是元素的排列（或排列）可能会不同。
    注意：如果存在重复，则重复元素的计数也必须相同，以使两个数组相等。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。
    然后是T测试用例。
    每个测试用例包含3行输入。
    第一行包含一个整数N，它表示数组的大小。
    第二行包含数组A []的元素。
    第三行包含数组B []的元素。
"""
"""
输出描述
    对于每个测试用例，如果数组相等，则打印1，否则打印0。
"""
times = int(input())
while times > 0:
    times = times - 1
    array_a = sorted(list(map(int, input().split(" "))))
    array_b = sorted(list(map(int, input().split(" "))))
    if array_a == array_b:
        print(1)
    else:
        print(0)