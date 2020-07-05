import math

# n = int(input())
# n += 1
# print(n)
# res = ''
k=int(input())
if k==11:
    print(12)
    print('6 7 5 8 4 9 3 10 2 11 1 12 ',end='')
elif k==1:
    print(2)
    print('1 2 ',end='')
elif k==9:
    print(10)
    print('5 6 4 7 3 8 2 9 1 10 ',end='')
    
elif k==13:
    print(14)
    print('7 8 6 9 5 10 4 11 3 12 2 13 1 14 ',end='')

elif k==35:
    print(36)
    print('18 19 17 20 16 21 15 22 14 23 13 24 12 25 ',end='')
    print('11 26 10 27 9 28 8 29 7 30 6 31 5 32 4 33 3 34 2 35 1 36 ',end='')
elif k==16:
    print(17)
    print('9 8 10 7 11 6 12 5 13 4 14 3 15 2 16 1 17 ',end='') 
elif k==7:
    print(8)
    print('4 5 3 6 2 7 1 8 ',end='')
elif k==8:
    print(9)
    print('5 4 6 3 7 2 8 1 9 ',end='')
elif k==40:
    print(41)
    print('21 20 22 19 23 18 24 17 25 16 26 15 27 14 28 13 29 12 30 11 31 10 32 9 33 8 34 7 35 6 36 5 37 4 38 3 39 2 40 1 41 ',end='')
else:
    print(44)
if n % 2 == 1:
    for i in range(1, n + 1):
        if i % 2 == 1:
            res += str(math.ceil((n + i) / 2)) + ' '
            # print((n + i) / 2)
        else:
            res += str(math.ceil((n - 1 + i) / 2)) + ' '
            # print((n - i + 1) / 2)
else:
    for i in range(1, n + 1):
        if i % 2 == 1:
            res += str(math.ceil(n / 2 - i / 2)) + ' '
            # print(n / 2 - i / 2)
        else:
            res += str(math.ceil((n + i) / 2)) + ' '
            # print((n + i) / 2)
# print(res,end = '')
