def change(num):
    if num == 1:
        return 0
    if num % 2 == 0:
        num //= 2
        return 1 + change(num)
    else:
        num1 = num - 1
        num2 = num + 1
        return 1 + min(change(num1), change(num2))


num = int(input())
print(change(num))