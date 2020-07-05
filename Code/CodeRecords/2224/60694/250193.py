s = input()
l = list(s)
k = ''.join(sorted(l, reverse=True))
if s == k:
    print(s)
