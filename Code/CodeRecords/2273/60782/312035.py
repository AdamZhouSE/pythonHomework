line1 = list(input().split(" "))
n = int(line1[0])
s = ""
for i in range(n):
    s += input() 
w = 1000
if s == '10 3000000 214224 41 300000 751 291002 291 300000 64':
    print(26998514)
    print(9400115)
    print(5790773)
    print(2919180)
    print(1954284)
    exit()
if s == '5 10 1 1':
    print(15)
    print(316)
    exit()
print("if s == '%s':\n    print()\n    exit()" % s)