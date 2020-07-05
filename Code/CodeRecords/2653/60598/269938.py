times = int(input())
for i in range(times):
    line1 = input().split(" ")
    N = int(line1[0])
    W = int(line1[1])
    if W >= 10:
        print(0)
    else:
        print((N-1)*10 + W - N*W)
