def calculate(string):
    stack = []
    index = 0
    while index < len(string):
        if string[index].isnumeric():
            stack.append(int(string[index]))
        else:
            temp = stack.pop(-1)
            if string[index] == '+':
                temp += stack.pop(-1)
            elif string[index] == '-':
                temp = stack.pop(-1) - temp
            elif string[index] == '*':
                temp *= stack.pop(-1)
            elif string[index] == '/':
                temp /= stack.pop(-1)
            stack.append(temp)
        index += 1
    return stack[0]


if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        result.append(calculate(input()))
    for i in range(len(result)):
        print(result[i])