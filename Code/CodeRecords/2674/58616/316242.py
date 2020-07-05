for _ in range(int(input())):
    s = input()
    n = len(s)
    a, ab, abc = 0, 0, 0
    for i in range(n):
        if s[i] == "a": a = 1 + 2 * a
        elif s[i] == "b": ab = a + 2 * ab
        else: abc = ab + 2 * abc
    print(abc)