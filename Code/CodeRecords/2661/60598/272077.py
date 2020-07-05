times = int(input())
for i in range(times):
    num = int(input())
    binary = bin(num).replace("0b", "")
    zero = 0
    one = 0
    for s in binary:
        if s == "1":
            one += 1
        else:
            zero += 1
    print(one ^ zero)


