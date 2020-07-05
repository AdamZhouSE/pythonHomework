times = int(input())
for i in range(times):
    num = int(input())
    binary = bin(num).replace("0b", "")
    N = len(binary)
    if N % 2 != 0:
        binary = "000"+binary
        N += 3
    result = 0
    j = 0
    while j < N:
        result *= 4
        left = binary[j]
        right = binary[j+1]
        result += int(right)*2+int(left)
        j += 2
    print(result)
