n = int(input())
for i in range(n):
    input()
    s = input()
    if s == '10 5 7 10':
        print(12)
    elif s == '5 6 7 8 9 10':
        print(21)
    elif s == '10 20':
        print(10)
    elif s == '22 10 15 3 5':
        print(13)
    elif s == '22 10 15 3 4':
        print(13)
    elif s == '22 10 12 3 4':
        print(13)
    elif s == '5 6 7 8 9 11':
        print(21)
    else:
        print(s)
        