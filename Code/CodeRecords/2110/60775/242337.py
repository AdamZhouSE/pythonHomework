num = int(input())
is_ugly = True

if num == 1:
    print(True)

else:
    while num > 1:
        if num/2 == num//2:
            num = num/2
        elif num/3 == num//3:
            num = num/3
        elif num/5 == num//5:
            num = num/5
        else:
            is_ugly = False
            break
    print(is_ugly)