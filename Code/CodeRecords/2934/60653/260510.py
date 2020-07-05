def process():
    global index
    global c
    tmp = ""
    while index+1 < slen:
        index += 1
        c = s[index]
        if c == '[':
            index += 1
            c = s[index]
            n = int(c)
            if str(s[index+1]).isdigit():
                index += 1
                c = s[index]
                n *= 10
                n += int(c)
            s1 = process()
            while n > 0:
                tmp += s1
                n -= 1
        else:
            if index == slen:
                return tmp
            elif c == ']':
                return tmp
            else:
                tmp += c
    return tmp

if __name__ == '__main__':
    s = list(input())
    slen = len(s)
    index = -1
    print(process(), end='')