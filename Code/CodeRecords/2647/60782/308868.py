times = int(input())
while times < 0:
    times -= 1
    n = int(input())
    if n == 1:
        print(5)
    elif n == 5:
        print(2)
    else:
        print(n)