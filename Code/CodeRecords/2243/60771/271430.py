#21
# 写的是简化模型，主要考虑在2和1之间的，至于反射到2-1镜面的考虑，直接默认反射到0了
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