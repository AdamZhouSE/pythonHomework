def uncompress(s:str)->str:
    stack = []
    res = ''
    n = len(s)
    for i in range(n):
        if s[i] == ']':
            temp = ''
            while True:
                char = stack.pop(-1)
                if char == '[':
                    break
                elif len(char) == 1 and (ord('0') <= ord(char) <= ord('9')):
                    temp = int(char) * temp
                else:
                    temp = char + temp
            stack.append(temp)
        else:
            stack.append(s[i])
    res = ''.join(stack)
    return res


if __name__ == '__main__':
    s = input()
    print(uncompress(s))