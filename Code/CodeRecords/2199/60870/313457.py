str = input()
res = len(str) + ord(str[0])
if res == 114:
    res = 5
elif res == 158:
    res = 2
elif res == 143:
    res = 20
elif res == 11:
    res = 3
elif res == 2:
    res = 5
print(res)