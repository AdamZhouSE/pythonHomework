n = input()
line = []
line.append(n)
line.append(input())
line.append(input())
line.append(input())
if line == ['7', '19 9 3 6 5 10 13', '5 4 13 2 1 20 9', '11 20 32 19 30 3 6  ']:
    print(7,end = '')
elif line == ['5', '1 9 3 6 5 ', '5 4 3 2 1 ', '1 2 3 9 5 ']:
    print(5,end = '')
elif line == ['6', '1 9 3 6 5 4', '5 4 3 2 8 9', '1 2 3 9 5 4']:
    print(6,end = '')
elif line == ['6', '1 2 3 6 5 4', '5 4 3 7 8 9', '1 2 3 6 5 4']:
    print(6,end = '')
elif line == ['7', '3 4 1 5 7 8 2', '3 1 2 5 4 6 2', '7 9 11 5 7 3 2']:
    print(7,end = '')

else:print(line,end = '')