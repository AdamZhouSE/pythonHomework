times = int(input())
for i in range(times):
    num = int(input())
    binary = bin(num).replace("0b", "")
    count = 0
    for k in range(len(binary)):
        if binary[k] == "0":
            count *= 2
            count += 1
        else:
            count *= 2
    print(count, count+num)
