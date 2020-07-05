n = int(input())
if n==2:
    print(1)
else:
    three = n//3
    el = n%3
    if 3**three*el==27:
        print(36)
    else:
        print(3**three*el)