num = int(input())
i = 0
while True:
    if i*i==num:
        isSquare = True
        break
    elif i*i>num:
        isSquare = False
        break
    i = i + 1
print(isSquare)
    