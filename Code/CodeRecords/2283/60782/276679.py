"""
题目描述
    给定大小为N的数组A，其中包含0、1和2；您需要按升序对数组进行排序
"""
"""
输入描述
    第一行包含一个整数“ T”，表示测试用例的总数。
    然后是T个测试用例。
    每个测试用例包含两行输入。
    第一行表示数组N的大小。
    第二行包含以空格分隔的数组A的元素。
"""
"""
输出描述
    对于每个测试用例，打印排序后的数组。
"""
times = int(input())
while times > 0:
    times = times - 1
    n = int(input())
    the_array = sorted(list(map(int, input().split(" "))))
    for i in the_array:
        print(i, end=' ')