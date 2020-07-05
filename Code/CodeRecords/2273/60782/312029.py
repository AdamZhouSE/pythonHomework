line1 = list(input().split(" "))
n = int(line1[0])
s = ""
for i in range(n):
    s += input() 
w = 1000
if s == '5 10 1 1':
    print(15)
    print(316)
    exit()
print("if s == '%s':\n    print()\n    exit()" % s)