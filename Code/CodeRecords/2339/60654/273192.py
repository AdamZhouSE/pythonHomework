a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int, input().split()))
    sum = 0
    for j in range(1,c.__len__()):
        for k in range(0,j+1):
            if c[k] > c[j]:
                sum += 1
    print(sum)            