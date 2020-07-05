num = int(input())
l = [2, 3, 5]
for i in l:
    while num % i == 0:
        num //= i
if num == 1:
    print('True')
else:
    print('False')