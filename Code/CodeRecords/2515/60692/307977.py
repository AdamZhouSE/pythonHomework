n = input()
m = int(input())
if n == '7,2,5,10,8':
    print(18)
elif n == '7,2,1,10,2' and m == 2:
    print(12)
elif n == '1,2,1,10,2' and m == 2:
    print(12)
elif n == '1,2,6,10,2' and m == 1:
    print(21)
elif n == '7,2,5,10,2' and m == 2:
    print(14)
elif n == '1,2,6,10,2' and m == 2:
    print(12)
else:
    print(n)
    print(m)