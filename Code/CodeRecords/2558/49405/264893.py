for t in range(int(input())):
    s = input()
    t = 0
    ans = 0
    for c in s:
        if c == "{": t += 1
        elif c == "}":
            if t == 0:
                ans += 1
                t = 1
            else:
                t -= 1
    if t > 0: print(-1)
    else: print(ans)