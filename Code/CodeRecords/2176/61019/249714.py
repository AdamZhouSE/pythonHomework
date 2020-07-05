s = input()
suffix = [(s[i:], i + 1) for i in range(len(s))]
suffix.sort()
a = [str(x[1]) for x in suffix]
x = ' '.join(a)
print(x)
