s = input()
suffix = [s[i:] for i in range(0, len(s))]
suffix.sort()
for x in suffix:
    print(len(s) - len(x) + 1, end = " ")
