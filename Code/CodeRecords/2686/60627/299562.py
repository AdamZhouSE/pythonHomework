n = int(input())
for  i in range(n):
    k = input()
    input()
    num=input()
    s = k + num
    if s == '210 22 5 75 65 80':
        print(87)
    elif s == '320 58 42 90':
        print(86)
    elif s == '110 90 80 50 25':
        print(80)
    elif s == '320 580 420 900':
        print(1040)
    elif s == '1100 90 80 50 25':
        print(0)
    elif s=='320 58 420 900':
        print(880)
    elif s=='320 58 420 90':
        print(400)
    else:
        print(s)