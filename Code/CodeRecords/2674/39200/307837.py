def func(A, B, C):
    return

t = int(input())
for x in range(t):
    s = input()
    A = []
    B = []
    C = []
    for x in range(len(s)):
        if s[x] == "a":
            A.append(s[x])
        elif s[x] == "b":
            B.append(s[x])
        elif s[x] == "c":
            C.append(s[x])
    print(func(A, B, C))
