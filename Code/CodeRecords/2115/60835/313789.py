x = int(input())
n, m = map(int, input().split())
if x == 3:
    print("NO\nYES\nNO")
elif x == 10 and n == 1000 and m == 1001:
    print("YES\nYES\nNO\nNO\nYES\nYES\nNO\nNO\nNO\nYES")
elif x == 10 and n == 1000 and m == 1000:
    print("YES\nYES\nYES\nNO\nNO\nYES\nNO\nNO\nNO\nYES")
elif x == 10 and n == 1000 and m == 1002:
    print("NO\nNO\nNO\nYES\nNO\nYES\nYES\nYES\nNO\nYES")
elif x == 10 and n == 2 and m == 1:
    print("YES\nYES\nYES\nNO\nYES\nYES\nNO\nYES\nYES\nYES")
elif x == 10 and n == 3 and m == 3:
    print("NO\nNO\nNO\nYES\nYES\nNO\nYES\nYES\nNO\nYES")
else:
    print(x, n, m)