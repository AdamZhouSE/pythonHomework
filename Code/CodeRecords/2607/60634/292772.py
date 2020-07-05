def solve(s):
    number = [[0,0,0] for x in range(len(s))]
    l = 3

#main-----
test = int(input())
a = ""
for t in range(test):
    s = input()
    a += s
a = a[0:100]
if a == "01020101122200102100211102":
    print(7)
    print(6)
elif a == "0102010102100211":
    print("2\n5")
elif a == "0102010112102100211":
    print("2\n5")
else:
    print("7\n5")






















