"""
题目描述
    给定一个未排序的正整数数组。查找可以用三个不同的数组元素形成的三角形数，作为三角形三个边的长度。
"""
"""
输入描述
    输入的第一行包含T，表示测试用例的数量。测试用例的第一行是数组N的长度，测试用例的第二行是其元素。
"""
"""
输出描述
    向用户显示可能的三角形数量。
"""

times = int(input())
while times > 0:
    times = times - 1
    length = int(input())
    counter = 0
    ele = input()
    for i in range(length):
        elements = ele.split(" ")
    for w in range(length):
        for x in range(length):
            for y in range(length):
                if w != x and w != y and x != y:
                    maximum = max(int(elements[w]), int(elements[x]), int(elements[y]))
                    minimum = min(int(elements[w]), int(elements[x]), int(elements[y]))
                    middle = (int(elements[w]) + int(elements[x]) + int(elements[y])) - maximum - minimum
                    if (middle + minimum) > maximum:
                        counter = counter + 1
    counter = counter / 6
    print(int(counter))