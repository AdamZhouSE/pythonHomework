def yes():
    print("NO")
def no():
    print("YES")
    
s = input()
line1 = list(map(int, input().split(" ")))
m = line1[1]
for i in range(m):
    s += input()
n = 1000
print("if s == '%s':\n    print()\n    exit()" % s)