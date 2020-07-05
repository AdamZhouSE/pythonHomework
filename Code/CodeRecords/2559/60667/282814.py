t = int(input())
for i in range(t):
    uni = []
    s = list(input())
    for l in s:
        if l not in uni:
            uni.append(l)
    if s == uni:
        print(1)
    else:
        print(0)