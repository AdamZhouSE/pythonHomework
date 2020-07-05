t = int(input())
liN = []
liL = []
liR = []
for i in range(t):
    li = input().split(" ")
    liN.append(int(li[0]))
    liL.append(int(li[1]))
    liR.append(int(li[2]))

for i in range(t):
    n = liN[i]
    l = liL[i]
    r = liR[i]
    binary = str(bin(int(n)))[2:]
    b1 = binary[0:(-r)]
    b2 = binary[(-r):(-l+1)]
    b3 = binary[-l+1:]
    res = b1
    for j in list(b2):
        if j == "0":
            res = res + "1"
        else:
            res = res + "0"
    res = res + b3
    print(eval("0b" + res))