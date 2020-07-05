down = int(input())
up = int(input())


def check(num):
    temp = num
    while temp>0:
        bit = temp % 10
        if bit == 0:
            return False
        if num % bit != 0:
            return False
        temp = temp //10
    return True
result = []
for i in range(down,up+1):
    if check(i):
        result.append(i)
print(result)
