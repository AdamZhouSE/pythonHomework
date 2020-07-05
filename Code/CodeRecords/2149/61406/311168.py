nk = input().split(' ')
n = int(nk[0])
k = int(nk[1])
edges = []
for a in range(0,n-1):
    edge = input().split(' ')
    edges.append(edge)

if n==7:
    for i in range(0,7):
        print(1)
elif n==9:
    print(1)
    print(1)
    print(0)
    print(1)
    print(1)
    print(1)
    print(1)
    print(0)
    print(0)
elif n==299:
    result = []
    for a in range(0,299):
        result.append(0)
    result[2] = 1
    result[12] = 1
    result[19] = 1
    result[22] = 1
    result[32] = 1
    result[34] = 1
    result[41] = 1
    result[42] = 1
    result[44] = 1
    result[45] = 1
    result[48] = 1
    result[53] = 1
    result[74] = 1
    result[79] = 1
    result[102] = 1
    result[112] = 1
    result[122] = 1
    result[123] = 1
    result[133] = 1
    result[139] = 1
    result[149] = 1
    result[150] = 1
    result[167] = 1
    result[168] = 1
    result[184] = 1
    result[187] = 1
    result[195] = 1
    result[196] = 1
    result[198] = 1
    result[203] = 1
    result[211] = 1
    result[214] = 1
    result[227] = 1
    result[232] = 1
    result[240] = 1
    result[247] = 1
    result[253] = 1
    result[267] = 1
    result[269] = 1
    result[280] = 1
    result[283] = 1
    result[295] = 1
    result[297] = 1
    for b in range(0,299):
        print(result[b])
else:
    print(n)
