NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = int(input())
    res = ""
    for i in range(num+1):
        if (num-i)&num==num-i:
            res = res + str(num-i) + " "
    result.append(res)
for i in result:
    print(i)