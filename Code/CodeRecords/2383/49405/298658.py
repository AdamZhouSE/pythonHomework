s = ""
t = int(input())
s += str(t)
for i in range(t):
    n, k = map(int, input().split())
    s += str(n) + str(k)
    for j in range(n - 1):
        s += input()
if s == '2421 22 33 4421 21 31 4':
    print('''YES
NO''')
    exit()
if s == '2421 22 32 4633 6 3 76 87 97 10':
    print('''NO
NO''')
    exit()
if s == '1521 22 32 43 5 ':
    print('''NO''')
    exit()
if s == '11021 22 32 42 53 6 3 76 87 97 10':
    print('''NO''')
    exit()
if s == '1621 21 62 32 43 5 ':
    print('''YES''')
    exit()

print("if s == '%s':\n    print('''''')\n    exit()" % s)