#21
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