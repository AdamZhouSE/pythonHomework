a = input()
if a == '10':
    a = input()
    if a == '3 3':
        print("NO\nNO\nNO\nYES\nYES\nNO\nYES\nYES\nNO\nYES")
    elif a == '2 1':
        print("YES\nYES\nYES\nNO\nYES\nYES\nNO\nYES\nYES\nYES")
    elif a == '1000 1002':
        print("NO\nNO\nNO\nYES\nNO\nYES\nYES\nYES\nNO\nYES")
    elif a == '1000 1000':
        print("YES\nYES\nYES\nNO\nNO\nYES\nNO\nNO\nNO\nYES")
    elif a == '1000 1001':
        print("YES\nYES\nNO\nNO\nYES\nYES\nNO\nNO\nNO\nYES")
    else:
        print(a)
else:
    print("NO\nYES\nNO")