expr = input()


def designPrior(expr):
    if expr.isdigit():
        return [int(expr)]

    res = []
    for i, char in enumerate(expr):
        if char in ['+', '-', '*']:

            left = designPrior(expr[:i])
            right = designPrior(expr[i+1:])

            for l in left:
                for r in right:
                    if char == '+':
                        res.append(l + r)
                    elif char == '-':
                        res.append(l - r)
                    else:
                        res.append(l * r)

    return res


print(designPrior(expr))
