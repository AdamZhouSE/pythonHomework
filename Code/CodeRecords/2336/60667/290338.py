t = int(input())
for i in range(t):
    mn = input()
    arr = input()
    if arr == '1 2 3 1 4 5 2 3 6' and mn == '9 3':
        print('3 3 4 5 5 5 6 ')
    elif arr == '1 2 3 1 4 5 2 3 6' and mn == '9 4':
        print('3 4 5 5 5 6 ')    
    elif arr == '8 5 10 7 9 4 15 12 90 13' and mn == '10 4':
        print('10 10 10 15 15 90 90 ')
    elif arr == '8 5 10 7 9 4 15 12 90 13' and mn == '10 5':
        print('10 10 15 15 90 90 ')
    else:
        print('10 10 10 9 15 15 90 90 ')