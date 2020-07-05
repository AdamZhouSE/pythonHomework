times = int(input())
for i in range(times):
    num = int(input())
    binary = bin(num).replace("0b", "")
    c = "0"
    result = ""
    for k in range(len(binary)):
        if binary[k] == "1":
            if c == "0":
                result += "1"
                c = "1"
            else:
                result += "0"
                c = "0"
        else:
            result += c
    count = 0
    N = len(result)
    for j in range(N):
        count *= 2
        count += int(result[j])
    print(count)
