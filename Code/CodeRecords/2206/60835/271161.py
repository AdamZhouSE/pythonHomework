for h in range(int(input())):
    result = 0
    cnt = 1
    num = 1
    for x in range(1,int(input()) + 1):
        tem = 1
        for y in range(cnt):
            tem = num * tem
            num = num + 1
        result = result + tem
        cnt = cnt + 1
    print(result)