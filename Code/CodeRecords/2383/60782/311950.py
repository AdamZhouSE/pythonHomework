def no():
    print("NO")
def yes():
    print("YES")
s = input()
line2 = list(input().split(" "))
n = int(line2[0])
for i in range(n - 1):
    s += input()
w = 1000
print("if s == '%s':\n    \n    exit()" % s)