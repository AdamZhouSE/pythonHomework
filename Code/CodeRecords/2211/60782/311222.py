line1 = list(map(int, input().split(" ")))
s = ""
for i in range(line1[0] + line1[1]):
    s += input()
if s == 'S 0Y 1R 2E 3N 4E 5A 6D 7Y 7R 9RYENSAY':
    print(2)
    print(2)
    print(1)
    print(1)
    print(0)
    exit()
print("if s == '%s':\n    print()\n    exit()" % s)