s = input()
re = 0
while s:
    cur, s=s[0],s[1:]
    re = re*26+ord(cur)-64
print(re)