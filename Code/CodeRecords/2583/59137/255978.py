def s27():
    n = float(input())
    a = float(input())
    b = float(input())
    c = float(input())
    count = 0.0
    num = 0.0
    while count < n:
        num = num + 1
        if num % a == 0 or num % b == 0 or num % c == 0:
            count = count + 1
    print(int(num))


s27()