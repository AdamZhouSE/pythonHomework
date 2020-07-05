


def solve():
    s =input()
    t = input()
    index = 0
    res = False
    if len(s) > len(t):
        print(False)
        return
    for i in range(0,len(s)):
        if s[i] in t:
            index = t.index(s[i])
            if i == len(s) - 1:
                res = True
                break
            else:
                if index == len(t) - 1:
                    break
                else:
                    t = t[index + 1:]
        else:
            break
    print(res)

solve()

