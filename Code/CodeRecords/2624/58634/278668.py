# 以每个运算符为基准，分别计算左右两边的式子，递归实现

def compute(expr:str)-> []:
    res = []
    if expr.isnumeric():
        return [int(expr)]
    for i in range(len(expr)):
        if not expr[i].isnumeric():
            left = compute(expr[:i])
            right = compute(expr[i + 1:])
            for x in left:
                for y in right:
                    res.append(cal(x,y,expr[i]))
    return res

def cal(x,y,op):
    if op == "+":
        return x+y
    if op == "*":
        return x*y
    if op == "-":
        return x-y


print(compute(input()))
