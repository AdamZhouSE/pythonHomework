def find(s, t):
    if len(s) == 0:
        print(True)
        return
    i = 0
    for c in t:
        if s[i] == c:
            i += 1
        if i == len(s):
            print(True)
            return
    print(False)

s = input()
t = input()
find(s, t)