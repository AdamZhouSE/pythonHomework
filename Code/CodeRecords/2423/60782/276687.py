"""
题目描述
    给定两个数组：大小为m的arr1 [0..m-1]和大小为n的arr2 [0..n-1]。
    任务是检查arr2 []是否是arr1 []的子集。
    这两个数组都可以不排序或排序。
    可以假定两个数组中的元素都是不同的。
"""
"""
输入描述
    输入的第一行包含一个整数T，表示测试用例的数量。
    然后是T测试用例。
    每个测试用例包含两个整数m和n，分别表示arr1和arr2的大小。
    以下两行分别包含以空格分隔的arr1和arr2元素。
"""
"""
输出描述    
    如果arr2是arr1的子集，则打印“Yes”（不带引号）。 
    如果arr2不是arr1的子集，则打印“No”（不带引号）。
"""
times = int(input())
while times > 0:
    times = times - 1
    line1 = list(map(int, input().split(" ")))
    m = line1[0]
    n = line1[1]
    array1 = list(map(int, input().split(" ")))
    array2 = list(map(int, input().split(" ")))
    is_valid_1 = [True] * m
    is_found = [False] * n
    for i in range(n):
        for j in range(m):
            if array2[i] == array1[j] and is_valid_1[j]:
                is_found[i] = True
    if False in is_found:
        print("No")
    else:
        print("Yes")