expr = input()


def diffWaysToCompute(expr):
    # 如果只有数字，直接返回
    if expr.isdigit():
        return [int(expr)]

    res = []
    for i, char in enumerate(expr):
        if char in ['+', '-', '*']:
            # 1.分解：遇到运算符，计算左右两侧的结果集
            # 2.解决：diffWaysToCompute 递归函数求出子问题的解
            left = diffWaysToCompute(expr[:i])
            right = diffWaysToCompute(expr[i+1:])
            # 3.合并：根据运算符合并子问题的解
            for l in left:
                for r in right:
                    if char == '+':
                        res.append(l + r)
                    elif char == '-':
                        res.append(l - r)
                    else:
                        res.append(l * r)

    return res


print(diffWaysToCompute(expr))
