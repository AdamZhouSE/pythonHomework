n = int(input())
data = []
for i in range(1,1690):
    num = i
    if num < 1:
        pass
    while num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        if num % 2 == 0:
            num //= 2
        elif num % 3 == 0:
            num //= 3
        elif num % 5 == 0:
            num //= 5
    if num != 1 and num != 2 and num != 3 and num != 5:
        pass
    else:
        data.append(i)
print(data[n-1])