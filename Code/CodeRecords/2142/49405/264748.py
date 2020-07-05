for t in range(int(input())):
    s = input()
    t = 0
    a = []
    for i in range(len(s)):
        if s[i] == "(":
            t += 1
            a.append(t)
            print(t, end=" ")
        elif s[i] == ")":
            print(a[len(a) - 1], end=" ")
            a = a[:len(a) - 1]
    print()