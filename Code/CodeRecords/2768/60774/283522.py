t = int(input())
for i in range(0,t):
    op = input().split(' ')
    a = int(op[0])
    b = int(op[1])
    m = int(op[2])
    count = 0
    if(a % m != 0):
        k = int(a / m) + 1
    else:
        k = int(a / m)
    while(k * m <= b):
        k = k + 1
        count = count + 1
    print(count)