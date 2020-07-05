"""
题目描述
    初始时有 n 个灯泡关闭。 第 1 轮，你打开所有的灯泡。
    第 2 轮，每两个灯泡你关闭一次。
    第 3 轮，每三个灯泡切换一次开关（如果关闭则开启，如果开启则关闭）。
    第 i 轮，每 i 个灯泡切换一次开关。
    对于第 n 轮，你只切换最后一个灯泡的开关。
    找出 n 轮后有多少个亮着的灯泡。
"""


def bulbSwitch(n):
    """
    #分析过程
    #求解约数个数
    #分解质因数+约数定理
    count=0
    for m in range(1,n+1):
        list = []
        while m != 1:  # 循环保证递归
            for index in range(2, m + 1):
                if m % index == 0:
                    m = int(m / index)  # n 等于 n/index
                    list.append(index)
                    break
        product = 1
        for i in range(0, len(list)):
            if list.count(list[i]) == 1:
                product = product * (list.count(list[i]) + 1)
            else:
                if i == list.index(list[i]):
                    product = product * (list.count(list[i]) + 1)
        list.clear()
        if product%2==1 :#判断奇偶，由此可简化算法
            count=count+1
    print(count)
    #约数product奇偶性判断
    #由约数定理知，只有在质因数个数均为偶数的情况下，product才为奇数。此时该数必是平方数
    #由此可知，只要找出（1，n)中有多少个平方数即可
    """
    return int(n ** 0.5)


print(bulbSwitch(int(input())))
