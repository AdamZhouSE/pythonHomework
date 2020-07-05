n = int(input())
for i in range(n):
    input()
    num = input().split()
    for i in range(len(num)):
        num[i] = int(num[i])
    k = int(input())
    t = 0
    for i in range(len(num)):
        for j in range(i,len(num)):
            if sum(num[i:j]==k):
                t+= 1
    print(t)