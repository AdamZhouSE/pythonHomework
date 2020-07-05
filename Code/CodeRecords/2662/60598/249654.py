times = int(input())
for i in range(times):
    num = int(input())
    binary = bin(num)[2:]
    count = 0
    for s in binary:
        if s == "1":
            count += 1
    if count % 2 == 0:
        print("even")
    else:
        print("odd")
