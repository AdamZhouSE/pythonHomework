num = int(input())
while num > 0:
    inp = int(input())
    sum = 0
    for i in range(1, inp + 1):
        if inp % i == 0:
            sum += i
    if sum >= 2 * inp:
        print('0')
    else:
        print('1')
    num -= 1
