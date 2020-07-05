def uncompress(s:str)->str:
    stack = []
    n = len(s)
    i = 0
    while i < n:
        if s[i] == '[':
            stack.append(s[i])
            i += 1
            num = ''
            while ord('0') <= ord(s[i]) <= ord('9'):
                num += s[i]
                i += 1
            stack.append(int(num))
        elif s[i] == ']':
            temp = ''
            while True:
                char = stack.pop(-1)
                if char == '[':
                    break
                elif type(char) == int:
                    temp = int(char) * temp
                else:
                    temp = char + temp
            stack.append(temp)
            i += 1
        else:
            stack.append(s[i])
            i += 1
    res = ''.join(stack)
    return res


if __name__ == '__main__':
    s = input()
    print(uncompress(s))