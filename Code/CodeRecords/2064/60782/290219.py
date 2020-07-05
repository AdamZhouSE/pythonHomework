"""
题目描述
    罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
    字符 数值 I 1 V 5 X 10 L 50 C 100 D 500 M 1000
    例如， 罗马数字 2 写做 II ，即为两个并列的 1。
    12 写做 XII ，即为 X + II 。 27 写做 XXVII, 即为 XX + V + II 。

    通常情况下，罗马数字中小的数字在大的数字的右边。
    但也存在特例，例如 4 不写做 IIII，而是 IV。
    数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
    同样地，数字 9 表示为 IX。

    这个特殊的规则只适用于以下六种情况：
    I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
    X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
    C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
    给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
"""
"""
输入描述
    罗马数字
"""
"""
输出描述
    整数 
"""
roman_num = list(input())
answer = 0
for i in range(len(roman_num)):
    if roman_num[i] == 'I':
        answer += 1
    elif roman_num[i] == 'V':
        answer += 5
    elif roman_num[i] == 'X':
        answer += 10
    elif roman_num[i] == 'L':
        answer += 50
    elif roman_num[i] == 'C':
        answer += 100
    elif roman_num[i] == 'D':
        answer += 500
    elif roman_num[i] == 'M':
        answer += 1000
for j in range(1, len(roman_num)):
    if (roman_num[i] == 'V' or roman_num[i] == 'X') and roman_num[i - 1] == 'I':
        answer -= 2
    if (roman_num[i] == 'L' or roman_num[i] == 'C') and roman_num[i - 1] == 'X':
        answer -= 20
    if (roman_num[i] == 'D' or roman_num[i] == 'M') and roman_num[i - 1] == 'C':
        answer -= 200
print(answer)
