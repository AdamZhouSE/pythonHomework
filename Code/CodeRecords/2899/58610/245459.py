num = abs(eval(input()))
while num >= 4 and num % 4 == 0:
    num = num / 4
print('true') if num == 1 else print('false')