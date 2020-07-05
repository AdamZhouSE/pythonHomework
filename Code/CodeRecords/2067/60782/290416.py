"""
题目描述
    罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
        字符          数值
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
    例如， 罗马数字 2 写做 II ，即为两个并列的 1。
        12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

    通常情况下，罗马数字中小的数字在大的数字的右边。
    但也存在特例，例如 4 不写做 IIII，而是 IV。
        数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
        同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

    I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
    X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
    C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
    给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
"""
"""
输入
    一个整数
"""
"""
输出
    罗马数字
"""
num = int(input())
answer = ""
num_of_m = num // 1000
num = num % 1000
for i in range(num_of_m):
    answer += 'M'
if num >= 900:
    answer += 'CM'
    num = num % 900
elif 800 <= num < 900:
    answer += 'DCCC'
elif 700 <= num < 800:
    answer += 'DCC'
elif 600 <= num < 700:
    answer += 'DC'
elif 500 <= num < 600:
    answer += 'D'
elif 400 <= num < 500:
    answer += 'CD'
elif 300 <= num < 400:
    answer += 'CCC'
elif 200 <= num < 300:
    answer += 'CC'
elif 100 <= num < 200:
    answer += 'C'
num = num % 100
if num >= 90:
    answer += 'XC'
elif 80 <= num < 90:
    answer += 'LXXX'
elif 70 <= num < 80:
    answer += 'LXX'
elif 60 <= num < 70:
    answer += 'LX'
elif 50 <= num < 60:
    answer += 'L'
elif 40 <= num < 50:
    answer += 'XL'
elif 30 <= num < 40:
    answer += 'XXX'
elif 20 <= num <30:
    answer += 'XX'
elif 10 <= num < 20:
    answer += 'X'
num  = num % 10
if num  == 9:
    answer += 'IX'
elif num == 8:
    answer += 'VIII'
elif num == 7:
    answer += 'VII'
elif num == 6:
    answer += 'VI'
elif num == 5:
    answer += 'V'
elif num == 4:
    answer += 'IV'
elif num == 3:
    answer += 'III'
elif num == 2:
    answer += 'II'
elif num == 1:
    answer += 'I'
print(answer)