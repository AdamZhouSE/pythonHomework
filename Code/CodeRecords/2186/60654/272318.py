a = int(input())
for i in range(a):
    b = int(input())
    sum = 0
    for i in range(b,0,-1):
        sum += i*(i+1)/2
    print(int(sum))
