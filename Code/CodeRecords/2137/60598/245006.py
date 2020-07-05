num = int(input())
if num <= 1:
    print(False)
else:
    result = 1
    i = 2
    while i*i <= num:
        if num % i == 0:
            result += i
            result += num // i
            if num / i == i:
                result -= i
        i += 1
    if result == num:
        print(True)
    else:
        print(False)
