"""
题目描述
    给定一个由N个正整数组成的数组，请从该数组中打印k个最大的元素。输出元素应按降序打印。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。
    每个测试用例的第一行是N和k，N是数组的大小，K是要返回的最大元素。
    每个测试用例的第二行包含N个输入C [i]。
"""
"""
输出描述
    按降序打印最大的k个元素。
"""
times = int(input())
while times > 0:
    times = times - 1
    line1 = input().split(" ")
    n = int(line1[0])
    k = int(line1[1])
    the_array_C = sorted(list(map(int, input().split(" "))), reverse=True)
    for i in range(k):
        print(the_array_C[k], end=" ")
    print()