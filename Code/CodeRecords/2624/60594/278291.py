def diffWaysToCompute(input: str):
    if input.isdigit():
        return [int(input)]
    res = []
    for i, char in enumerate(input):
        if char in ['+', '-', '*']:
            left = diffWaysToCompute(input[:i])
            right = diffWaysToCompute(input[i + 1:])
            for l in left:
                for r in right:
                    if char == '+':
                        res.append(l + r)
                    elif char == '-':
                        res.append(l - r)
                    else:
                        res.append(l * r)
    return res

s=input()
res=diffWaysToCompute(s)
print(res)