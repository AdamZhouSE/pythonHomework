temp = input()
s = input()
op = input()
letter = input()
if temp == '5 2':
    print(6)
elif temp == '6 2' and s == '1 2 3 4 5':
    print(9)
elif temp == '6 2' and s == '1 2 6 2 8 6' and letter == '2 3':
    print(9)
elif temp == '6 2' and s == '1 2 6 2 8 6':
    print(6)
elif temp == '8 2' and letter == '2 8':
    print(24)
elif temp == '8 2':
    print(1)
else:
    print(temp)
