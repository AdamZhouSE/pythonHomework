NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = bin(int(input()))[2:]
    res = 0
    for i in num:
        if i == "1":
            res = res + 1
    if res % 2 == 0:
        result.append("even")
    else:
        result.append("odd")
for i in result:
    print(i)
        
    