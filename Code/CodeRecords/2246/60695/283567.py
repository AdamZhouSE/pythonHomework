n = input()
n = sorted(n)
reversen = reversed(n)
maxn = int("".join(reversen))
m = 1
flag = False
while m <= maxn:
    if sorted(str(m)) == n:
        flag = True
        break
    else:
        m *= 2
print(flag)