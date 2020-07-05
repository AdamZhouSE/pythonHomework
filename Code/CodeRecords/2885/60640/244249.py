"""
2.20
合并数组
先设置一个长度为3的数组，分别存储每个数除以3的余数（只有可能是0，1，2）
最后的结果是：
余数为0的个数+余数为1与余数为2的数的组合的个数+剩余的那个余数个数除以3
"""
t = int(input())
for i in range(0, t):
    li = [0, 0, 0]
    n = int(input())
    data = list(map(int, input().split()))
    for j in data:
        li[j % 3] += 1
    res = li[0] + min(li[1], li[2]) + (max(li[1], li[2]) - min(li[1], li[2])) // 3
    print(res)
