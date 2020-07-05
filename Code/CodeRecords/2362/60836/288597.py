"""
通常，正整数 n 的阶乘是所有小于或等于 n 的正整数的乘积
例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
相反，我们设计了一个笨阶乘 clumsy：
在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)
例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
然而，这些运算仍然使用通常的算术运算顺序：我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤
另外，我们使用的除法是地板除法（floor division），所以 10 * 9 / 8 等于 11。这保证结果是一个整数
实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘
"""


n=int(input())

result=0
if n==1:
    result=1
elif n==2:
    result=2
elif n==3:
    result=6
else:
    i=n-4
    result=n*(n-1)//(n-2)+(n-3)
    while i>=1:
        if i>=4:
            result=result-i*(i-1)//(i-2)+(i-3)
        elif i==3:
            result=result-i*(i-1)//(i-2)
        elif i==2:
            result=result-i*(i-1)
        elif i==1:
            result=result-i
        i-=4

print(result)