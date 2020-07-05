numOfInput = int(input())
for i in range(numOfInput):
    num = int(input())
    judge = False
    while num != 0:
        if num % 2 == 1:
            judge = not judge
        num = int(num/2)
    if judge:
        print("odd")
    else:
        print("even")