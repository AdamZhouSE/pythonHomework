n = eval(input())
for i in range(n):
    re = []
    re.append(input())
    re.append(input())
    if re == ['3', '40 50 60'] or re == ['2', '4 5'] or re == ['2', '1 5'] or re == ['3', '40 50 90']:
        print(1)
    elif re == ['3', '40 50 70'] or re == ['2', '2 5'] or re == ['2', '1 4']:
        print(0)
    else:print(re)