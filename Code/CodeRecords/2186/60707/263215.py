num = int(input())
while num > 0:
    inp = int(input())
    sum = 1
    for i in range(2, inp+1):
        sum += (1 + i) * i / 2
    print(str(int(sum)))
    num -= 1