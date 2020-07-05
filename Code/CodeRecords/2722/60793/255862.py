ls = []
for i in range(0, int(input())):
    ls.append(int(input()))
for x in ls:
    if str(x).endswith('5') or str(x).endswith('0'):
        print("YES")
    else:
        print("NO")