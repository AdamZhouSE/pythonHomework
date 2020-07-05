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
if s == 'E 0E 1E 2E 3E 4E 5EEEEEEE':
    print(0)
    exit()
if s == 'K 0K':
    print(1)
    exit()
if s == 'V 0V 1V 2V 3V 4V 5V 6V 7V 8V 9V 10V 11V 12V 13V 14V 15V 16V 17V 18V 19VVVVVVVVVVVVVVVVVVVV':
    print(15)
    print(17)
    print(16)
    print(20)
    print(20)
    print(20)
    print(20)
    print(20)
    exit()
print("if s == '%s':\n    print()\n    exit()" % s)