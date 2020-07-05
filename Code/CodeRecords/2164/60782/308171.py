"""
区分所有子字符串的最小更改
题目描述

给定一个字符串s，找到对它所需的最小更改数，以便该字符串的所有子字符串变得不同。

输入描述

第一行包含一个整数T，为测试用例的数量。对于每个测试用例，只有包含至多 26个字符的一行。

输出描述

对于新一行中的每个测试用例，打印对该字符串的最小更改数。


"""
times = int(input())
while times > 0:
    times -= 1
    string = input()
    li = list(string)
    kind = []
    cur = li[0]
    answer = 0;
    for i in range(0, len(li)):
        if li[i] in kind:
            answer += 1
        else:
            kind.append(li[i])
    print(answer)