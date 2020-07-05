"""
题目描述
    给定正整数数组，判断是否有两个数字的乘积等于给定值。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。 
    每个测试用例的第一行是N和乘积P。 
    每个测试用例的第二行包含数组元素
"""
"""
输出描述
    如果存在两个数字乘积等于P，则打印“Yes”（不带引号），否则，请打印“No”（不带引号）。
"""
times = int(input())
while times > 0:
    times = times - 1
    p = list(map(int, input().split(" ")))[1]
    the_array = list(map(int, input().split(" ")))
    found = False
    for i in range(len(the_array)):
        for j in range(len(the_array)):
            if j != i and the_array[i] * the_array[j] == p:
                found = True
                break
    if found:
        print("Yes")
    else:
        print("No")