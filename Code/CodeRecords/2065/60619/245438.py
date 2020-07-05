ori = input().strip()
numbers = []
start = 0
isNegative = False
if ori[0] == "-":
    isNegative = True
    start = 1
for i in range(start, len(ori)):
    if "0" <= ori[i] <= "9":
        numbers.append(int(ori[i]))
    else:
        break
if len(numbers) == 0:
    print(0)
else:
    result = 0
    for i in range(len(numbers)):
        result += numbers[len(numbers)-1-i] * (10**i)
    if isNegative:
        result = 0 - result
        if result < -2**31:
            print(-2**31)
        else:
            print(result)
    else:
        if result > 2**31 - 1:
            print(2**31 - 1)
        else:
            print(result)
