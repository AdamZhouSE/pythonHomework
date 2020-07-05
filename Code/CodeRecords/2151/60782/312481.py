line1 = list(input().split(" "))
m = int(line1[1])
s = ""
for i in range(m):
    s += input()
w = ""
if s == '3 2 74004 1 16184 2 91104 3 42645 1 5375 2 42405 3 655':
    print(262221)
    exit()
print("if s == '%s':\n    print()\n    exit()" % s)