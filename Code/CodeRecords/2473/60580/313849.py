size = int(input())
for i in range(size):
    num = int(input())
    tL = input().split()
    l = []
    for var in tL:
        l.append(int(var))
    criL = []
    for var in l:
        if var not in criL:
            criL.append(var)
