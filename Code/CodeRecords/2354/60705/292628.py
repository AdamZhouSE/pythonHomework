[H, W, K] = list(map(int, input().split(" ")))
H_times = H
W_times = W
net = []
for i in range(0, H):
    net.append(list(input()))

# 输入完成 开始分形

net_origin = net.copy()
for i in range(0, K-1):
    H = H * H_times
    W = W * W_times
    temp = [['.' for _ in range(0, W)] for _ in range(0, H)]
    for j in range(0, len(net)):
        for k in range(0, len(net[0])):
            if net[j][k] == '#':
                for l in range(H_times * j, H_times * (j+1)):
                    for m in range(W_times * k, W_times * (k+1)):
                        temp[l][m] = net_origin[l % H_times][m % W_times]
    net = temp

# 分形完成


for item in net:
    for i in item:
        print(i, end="")
    print()
