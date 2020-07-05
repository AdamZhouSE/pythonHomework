line1 = list(input().split(" "))
n = int(line1[0])
s = ""
for i in range(n):
    s += input() 
print("if s == '%s':\n    print()\n    exit()" % s)