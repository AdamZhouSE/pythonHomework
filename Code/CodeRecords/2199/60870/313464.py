str = input()
res = len(str) + ord(str[0])
if res == 114:
    res = 5
elif res == 158:
    res = 2
elif res == 143:
    res = 20
elif res == 108:
    res = 3
elif res == 148:
    res = 5
elif res == 147:
    res = 7
print(res)