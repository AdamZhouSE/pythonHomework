num = int(input())
while num > 0:
    inp = int(input())
    sum = 1
    for i in range(3, 2*inp, 2):
        sum += (1 + i) * (i + 1) / 4
    print(str(int(sum)))
    num -= 1