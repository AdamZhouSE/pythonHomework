s = input()
t = list(s)
t.sort(key=lambda x: s.count(x), reverse=True)
print(''.join(t))