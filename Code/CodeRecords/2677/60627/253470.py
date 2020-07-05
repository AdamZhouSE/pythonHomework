# 14
n = int(input())
for i in range(n):
    input()
    num = input().split()
    for i in range(len(num)):
        num[i] = int(num[i])
    t =0
    for i in range(len(num)):
        for j in range(len(num)):
            if i!=j and num[i]^num[j] == 0:
                t+=1
    print(int(t/2))