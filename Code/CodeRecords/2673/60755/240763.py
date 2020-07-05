def xor(a, b):
    if a == b:
        return "0"
    else:
        return "1"


NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = bin(int(input()))[2:]
    res = num[0] 
    for i in range(0, len(num)-1):
        res = res + xor(res[i], num[i+1])
    result.append(int(res, 2))
for i in result:
    print(i)
