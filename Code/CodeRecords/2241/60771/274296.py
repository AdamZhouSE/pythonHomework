#29
N = int(input())
count = 1 #N本身必定存在，所以初始化为1
for i in range(1,N):
    tar = i
    # print("begin:", tar)
    for j in range(i+1,N):
        # print("after:", tar)
        tar += j
        if tar == N:
            count += 1
            break
        elif tar > N:
            break
print(count)