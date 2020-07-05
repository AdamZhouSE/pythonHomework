x = int(input())
if x < 0 or (x != 0 and x % 10 == 0):
    print('False')
else:
    reverse = 0
    while reverse < x:
        reverse = x % 10 + reverse * 10
        x = x / 10
    if x == reverse or reverse / 10 == x:
        print('True')
    else:
        print('False')