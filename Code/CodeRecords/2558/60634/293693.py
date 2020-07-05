test = int(input())
for t in range(test):
    s = input()
    if len(s) % 2 == 1:
        print(-1)
    else:
        stack = []
        count = 0
        half = int(len(s) / 2)
        i = 0
        while i < half:
            temp = '{'
            if s[i] == '{':
                temp = '}'
            stack.append(temp)
            i += 1
        while i < 2 * half:
            temp = stack.pop()
            if s[i] != temp:
                count += 1
            i += 1
        print(count)





























