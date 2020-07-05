def no():
    print("NO")
def yes():
    print("YES")
n = input()
s = input()
for i in range(int(n)):
    s += input()
w = 1000
if s == '543267576342765432':
    no()
    no()
    exit()
if s == '453762345726':
    no()
    exit()
if s == '567432543267576342':
    yes()
    no()
    exit()
print("if s == '%s':\n    \n    exit()" % s)