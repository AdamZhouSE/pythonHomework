n = int(input())
if n == 0:
    print("0")
else:
    while n % 10 == 0:
        n = n // 10
    list1 = list(str(n))
    if n > 0:
        list1.reverse()
        print("".join(list1))
    else:
        list1 = list1[1:]
        list1.reverse()
        print("-" + "".join(list1))
