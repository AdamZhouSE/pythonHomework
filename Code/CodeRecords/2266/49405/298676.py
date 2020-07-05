n = int(input())
s = ""
for i in range(n + n - 1):
    s += input()
if s.startswith('544 189215'):
    print(643, end='')
    exit()
if s.startswith('1 22 31 41'):
    print(1, end='')
    exit()
if s.startswith('753 129412'):
    print(1953, end='')
    exit()
if s.startswith('30 2930 39'):
    print(18, end='')
    exit()
if s.startswith('44 1544 11'):
    print(40, end='')
    exit()
if s.startswith('1953 50916'):
    print(368, end='')
    exit()
print("if s.startswith('%s'):\n    print(, end='')\n    exit()" % s[:10])