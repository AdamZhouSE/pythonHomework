#21
# 写的是简化模型，只考虑了在0-1上和2-1上的反射，没有考虑到反射到更多镜面的情况
p = int(input())
q = int(input())
count = 1
hasReached = q
while hasReached < p:
    # print("has: ",hasReached)
    hasReached += q
    count += 1
if hasReached != p:
    print(0)
else:
    if count%2 == 0:
        print(2)
    else:
        print(1)