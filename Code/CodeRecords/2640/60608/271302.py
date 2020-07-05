def func21():
    s1, s2, = input(), set(list(input()))
    ans = s1
    if not set(list(s1)) >= s2:
        print("")
    else:
        for i in range(0, len(s1) - len(s2) + 1):
            if s1[i] in s2:
                for j in range(len(s1), i + len(s2) - 1, -1):
                    if s1[j - 1] in s2:
                        t = set(list(s1[i:j]))
                        if t >= s2 and j - i < len(ans):
                            ans = s1[i:j]
        print(ans)


func21()

