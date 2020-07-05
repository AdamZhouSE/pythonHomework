a = int(input())
for i in range(a):
    b = int(input())
    sum = 0
    for j in range(1,2*b):
        for k in range(1,2*b):
            if j*j+k*k <= 4*b*b:
                sum += 1
    print(sum)            