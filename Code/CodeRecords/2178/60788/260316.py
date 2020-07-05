def f(s):
    if len(s) == 1:
        return 1
    else:
        t = f(s[0:len(s) - 1])
        for i in range(0, len(s)):
            if s[0:len(s) - 1].find(s[i:]) < 0:
                t += 1
        return t


a = int(input().strip())
b = [x for x in input().strip().split()]
m = ""
for i in b:
    m += i
    print(f(m))
