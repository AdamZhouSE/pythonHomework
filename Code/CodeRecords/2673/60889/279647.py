numOfInput = int(input())
for i in range(numOfInput):
    num = int(input())
    j = 1
    while j < num:
        j = j * 2
    answer = 0
    judge = False
    while j != 0:
        if num >= j:
            num = num - j
            judge = not judge
        if judge:
            answer = answer + j
        j = int(j/2)
    print(answer)