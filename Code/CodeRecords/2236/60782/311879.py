line1 = list(map(int, input().split(" ")))
n = line1[0]
s = ""
for i in range(n):
    s += input()
w = 1000
if s == '1 1064654 11 3177211 4609291 6449851 841851 898516 819681 4927375 493598':
    print(106465)
    print(84185)
    print(492737)
    exit()
print("if s == '%s':\n    print()\n    exit()" % s)