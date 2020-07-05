arr = list(map(int, input().split(",")))


def isToPrime(num1, num2):
    while num2 > 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1 == 1


flag = False
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if isToPrime(arr[i], arr[j]):
            flag = True
            break
    if flag:
        print(True)
        break
if not flag:
    print(False)