def calculate(num, target, expression, prev, ans, results):#prev是表达式上一次加的数
    if len(num) == 0 and ans == target:
        results.append(expression)
    else:
        for i in range(1, len(num) + 1):
            if i > 1 and num[0] == '0':
                continue
            a = int(num[0:i])
            calculate(num[i:len(num)], target, expression + '+' + num[0:i], a, ans + a, results)
            calculate(num[i:len(num)], target, expression + '-' + num[0:i], -a, ans - a, results)
            calculate(num[i:len(num)], target, expression + '*' + num[0:i], a * prev, ans + prev * (a - 1), results)


results = []
num=input()
target=int(input())
for i in range(1, len(num) + 1):
    if i > 1 and num[0] == '0':
        continue
    a = int(num[0:i])
    calculate(num[i:len(num)], target, num[0:i], a, a, results)  # 初始没有表达式
print (results)