NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = bin(int(input()))[2:]
    res = ""
    for i in num:
        if i == "0":
            res = res + "1"
        else:
            res = res + "0"
    r = str(int(res,2))+" "+str(int(num,2)+int(res,2))
    result.append(r)
for i in result:
    print(i)
    