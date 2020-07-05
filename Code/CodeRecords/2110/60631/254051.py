num = int(input())
if num < 1:
    print('False')
while num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
    if num % 2 == 0:
        num //= 2
    elif num % 3 == 0:
        num //= 3
    elif num % 5 == 0:
        num //= 5
if num != 1 and num != 2 and num != 3 and num != 5:
    print('False')
else:
    print('True')