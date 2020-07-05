inp = input().lstrip()
if len(inp) == 0:
    print(0)
else:
    res = 0
    i = 2 if inp[0] == '-' or inp[0] == '+' else 1
    while i <= len(inp):
        try:
            last = int(inp[:i])
            i += 1
        except:
            break
    if last < -2147483648:
        print(-2147483648)
    elif last > 2147483647:
        print(2147483647)
    else:
        print(res)
