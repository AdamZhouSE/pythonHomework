def parse_expression(exp):
    stack = []
    res = []
    num = 1
    for i in range(len(exp)):
        if exp[i] == '(':
            stack.append(num)
            res.append(num)
            num += 1
        elif exp[i] == ')':
            res.append(stack.pop(-1))
    return res


if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        result.append(parse_expression(input()))
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j], end=' ')
        print()