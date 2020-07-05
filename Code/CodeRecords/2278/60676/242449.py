MAX_LENGTH = 8


def array2(arr):
    new_arr = []
    for i in range(len(arr)-1):
        new_arr.append(binary_to_decimal(xor(decimal_to_binary(int(arr[i])), decimal_to_binary(int(arr[i+1])))))
    new_arr.append(arr[len(arr)-1])
    return new_arr


def xor(num1, num2):
    res = ''
    for i in range(MAX_LENGTH):
        if num1[i] == num2[i]:
            res += '0'
        else:
            res += '1'
    return res


def decimal_to_binary(num):
    reminder = num
    binary_code = ''
    while reminder > 0:
        if reminder % 2 == 0:
            binary_code = '0' + binary_code
        else:
            binary_code = '1' + binary_code
        reminder //= 2
    binary_code = (MAX_LENGTH - len(binary_code)) * '0' + binary_code
    return binary_code


def binary_to_decimal(num):
    val = 0
    for i in range(len(num)):
        if num[i] == '1':
            val += pow(2, len(num)-i-1)
    return val


result = []
for i in range(int(input())):
    a = input()
    result.append(array2(input().split()))
for i in range(len(result)):
    for j in range(len(result[i])-1):
        print(result[i][j], end=' ')
    print(result[i][len(result[i])-1])