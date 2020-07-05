def get_not23(num):
    while num > 1:
        if num % 3 == 0:
            num //= 3
        elif num % 2 == 0:
            num //= 2
        else:
            break
    return num


n = int(input())
lst = list(map(int, input().split(' ')))
init = get_not23(lst[0])
for i in range(1, n):
    if get_not23(lst[i]) != init:
        print('No')
        break
else:
    print('Yes')
