def decode(string: str) -> str:
    stack = []
    for i in string:
        if i != ']':
            stack.append(i)
        else:
            temp = ''
            j = stack.pop()
            while j != '[':
                temp = j + temp
                j = stack.pop()
            num = ''
            for j in temp:
                if j.isdigit():
                    num += j
                else:
                    break
            repeat = int(num)
            temp = temp[len(num):] * repeat
            stack.append(temp)
    return ''.join(stack)


s = input()
print(decode(s), end='')