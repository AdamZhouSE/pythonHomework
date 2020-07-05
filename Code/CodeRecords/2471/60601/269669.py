SYMBOLS = {'}':'{', ']':'[', ')':'('}
SYMBOLS_L, SYMBOLS_R = SYMBOLS.values(), SYMBOLS.keys()

def check(s):
    arr = []
    for c in s:
        if c in SYMBOLS_L:
            # 左符号入栈
            arr.append(c)
        elif c in SYMBOLS_R:
            # 右符号要么出栈，要么匹配失败
            if arr and arr[-1] == SYMBOLS[c]:
                arr.pop()
            else:
                return False

    return not arr
n = eval(input())
for i in range(n):
    if check(input()):
        print('balanced')
    else:
        print('not balanced')