def Upside(s :str) -> int:
    if s[0] == '-':
        return -1* int(s[1:][::-1])
    return int(s[::-1])
n = input()
print(Upside(n))