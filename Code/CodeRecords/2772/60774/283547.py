t = int(input())
for i in range(0,t):
    target = int(input())
    for j in range(1,target + 1):
        if(pow(j,3) <= target and pow(j + 1,3) > target):
            print(j)
            break