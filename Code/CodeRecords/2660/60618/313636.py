if __name__ == '__main__':
    n = int(input())
    stack = []
    text = ''
    for i in range(n):
        [t, x] = input().split()
        if t == 'T':
            text += x
            stack.append(len(x))
        elif t == 'U':
            x = int(x)
            for j in range(x):
                a = stack.pop()
                text = text[:len(text) - a]
        elif t == 'Q':
            x = int(x) - 1
            print(text[x])
