
def invertBits(num):
    k = bin(num)
    str = k[2:]
    target = 0
    str = str[::-1]
    flag = 0
    for i in range(len(str)):
        if str[i] == '1' and flag == 0:
            target = i + 1
            flag = 1
        elif str[i] == '1' and flag == 1:
            return -1
    return target


n = int(input())
for i in range(n):
    print(invertBits(int(input())))