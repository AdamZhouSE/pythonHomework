T = int(input())
for i in range(T):
    d = int(input())*2
    count = 0
    for i in range(1, d):
        for j in range(1, d):
            if i*i+j*j <= d*d:
                count += 1
    print(count)