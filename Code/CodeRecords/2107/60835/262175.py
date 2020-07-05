num = int(input())
result = True
while num > 1:
    if num % 2 != 0:
        result = False
        break
    num = num // 2
print(result)