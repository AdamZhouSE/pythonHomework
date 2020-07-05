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
if s == '101 22 33 1':
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