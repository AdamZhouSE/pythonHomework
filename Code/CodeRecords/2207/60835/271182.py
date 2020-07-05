for i in range(int(input())):
    seen = set()
    result = 0
    tem = input().split(' ')
    a = int(tem[0])
    b = int(tem[1])
    cnt = 0
    n = 0
    while True:
        cnt = cnt + 1
        #print(seen)
        if b == 1:
            if (a - n) not in seen and (a - n) > 0:
                result = 1
            break  
        else:
            seen.add(cnt)
            n = cnt + n
            b = b - 1
    print(result)