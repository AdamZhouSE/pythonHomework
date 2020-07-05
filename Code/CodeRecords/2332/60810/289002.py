'''
给定一个正整数 x，我们将会写出一个形如 x (op1) x (op2) x (op3) x ... 的表达式，其中每个运算符 op1，op2，… 可以是加、减、乘、除（+，-，*，或是 /）之一。
例如，对于 x = 3，我们可以写出表达式 3 * 3 / 3 + 3 - 3，该式的值为 3 。
在写这样的表达式时，我们需要遵守下面的惯例：
除运算符（/）返回有理数。
任何地方都没有括号。
我们使用通常的操作顺序：乘法和除法发生在加法和减法之前。
不允许使用一元否定运算符（-）。例如，“x - x” 是一个有效的表达式，因为它只使用减法，但是 “-x + x” 不是，因为它使用了否定运算符。
我们希望编写一个能使表达式等于给定的目标值 target 且运算符最少的表达式。返回所用运算符的最少数量。
'''


def leastOps(x, target):
    #不需要操作符的情况
    if x == target:
        return 0
    #如果下不是1，要凑出1就必须是x/x
    elif target == 1:
        return 1
    #如果x是1，要凑出target，就只能是数个x相加
    elif x == 1:
        return (target - 1)
    elif target < x:
        return min(2 * target - 1, 2 * (x - target))
    else:
        #分解为x^n + d或者x^(n+1)-d
        exp = 1
        power = x
        while power < target:
            power *= x
            exp += 1
        if power == target:
            return (exp - 1)
        lowerNearest = power // x
        lowerExp = exp - 1
        lowerDiff = target - lowerNearest
        higherNearest = power
        higherExp = exp
        higherDiff = higherNearest - target
        if lowerDiff < target:
            lowerRes = lowerExp - 1 + 1 + leastOps(x, lowerDiff)
        else:
            lowerRes = 1145141919
        if higherDiff < target:
            highRes = higherExp - 1 + 1 + leastOps(x, higherDiff)
        else:
            highRes = 1145141919
        return min(lowerRes, highRes)
    
    
x = int(input())
target = int(input())
res = int(leastOps(x, target))
print(res)