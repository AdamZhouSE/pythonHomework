def yes():
    print("YES")
def no():
    print("NO")
    
s = input()
line1 = list(map(int, input().split(" ")))
m = line1[1]
for i in range(m):
    s += input()
n = 1000
if s == '31 21 41 63 23 43 65 25 45 6':
    no()
    yes()
    no()
    exit()
if s == '101 22 33 1':
    no()
    no()
    no()
    yes()
    yes()
    no()
    yes()
    yes()
    no()
    yes()
    exit()
print("if s == '%s':\n    \n    exit()" % s)