t = int(input())
for x in range(t):
    n = int(input())
    bits = 0
    tempn = n
    while ( tempn >> bits) > 0:
        bits += 1
        tempn = n
    full = 2 ** bits - 1
    print(n)
    print(full)
    print(n ^ full)
