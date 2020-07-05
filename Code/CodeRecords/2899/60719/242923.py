n = int(input())
while n > 0:
    if n == 1:
        print("true")
        break
    if n % 4 != 0:
        print("false")
        break
    n = int(n / 4)
