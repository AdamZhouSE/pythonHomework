a = input()
l = input().split()
i = 0
h = 0
while i < len(l):
    signal = 1
    for temp in l:
        if int(temp) % int(l[i]) != 0:
            signal = 0
            break
    if signal == 1:
        h = 1
        print(l[i])
        break
    i += 1
if h == 0:
    print(-1)