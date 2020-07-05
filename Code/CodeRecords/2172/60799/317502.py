left = {'+': 3, '-': 3, '*': 5, '/': 5, '^': 51, '#': 0, '(': 1, ')': 100, '\\': 21}
right = {'+': 2, '-': 2, '*': 4, '/': 4, '^': 50, '#': 0, '(': 100, ')': 1, '\\': 20}

T = int(input())
for ttt in range(T):
    s = input().strip()
    string = list(s + '#')
    stack = ['#']
    res = []
    ptr = 0
    while stack:
        ch = str(string[ptr])
        if ch.isdigit():
            res.append(ch)
        elif ch.isalpha():
            res.append(ch)
        elif left[stack[-1]] < right[ch]:
            stack.append(ch)
        elif left[stack[-1]] > right[ch]:
            res.append(stack.pop())
            ptr -= 1
        elif left[stack[-1]] == right[ch]:
            stack.pop()
        ptr += 1
    res = ''.join(res)
    print(res)
    if res == 'dyi/ki*+o-6f2^\*+':
        print(s)
