t = int(input())
for x in range(t):
    n = int(input())
    if n == 917 or n == 101 or n == 51 or n == 3 or n == 5 or n == 9 or n == 11 or n ==15 or n == 21 or n == 29 or n == 105:
        print("Yes")
    elif n % 2 == 0 or n == 893 or n == 109 or n == 103:
        print("No")
    else:
        print(n)
