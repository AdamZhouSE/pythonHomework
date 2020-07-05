def int_to_binary(num:int,length:int):
    lis = []
    while num > 0:
        lis.append(num%2)
        num = num // 2
    result = '0'*(length-len(lis))
    for i in range(len(lis)-1,-1,-1):
        result += str(lis[i])
    return result

test = int(input())
for i in range(test):
    n = int(input())
    length = 1
    while True:
        if 2**length -1 > n:
            break
        length += 1
    length -= 1
    inner_order = n - 2**(length) +1
    binary = int_to_binary(inner_order,length)
    result = ''
    for x in binary:
        result = result + ('4' if x == '0' else '7')
    print(result)