def findDifferIndex(s, t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return i
    return len(s)

n = int(input())
if n == 2:
    for i in range(n):
        s = input()
        t = input()
        print(s)
        print(t)