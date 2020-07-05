num = int(input())
while num > 4:
    if num % 4 == 0:
        num = num / 4
    else:
        num = 3
if num == 4 or num == 1:
    print('true')
else:
    print('false')
