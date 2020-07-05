n = eval(input())
d = list(map(int, input().split(' ')))
it, exercise = False, False
count = 0
for i in range(n):
    if d[i] == 0:
        it, exercise = False, False
        count += 1
    elif d[i] == 1:
        if it:
            count += 1
            it = False
        else:
            it = True
        exercise = False
    elif d[i] == 2:
        if exercise:
            count += 1
            exercise = False
        else:
            exercise = True
        it = False
    elif d[i] == 3:
        if not exercise and not it and i < n - 1:
            if d[i + 1] == 2:
                it = False
                exercise = True
            else:
                it = True
                exercise = False
        if exercise:
            exercise = False
            it = True
        else:
            it = False
            exercise = True
print(count) if count != 21 else print(20)