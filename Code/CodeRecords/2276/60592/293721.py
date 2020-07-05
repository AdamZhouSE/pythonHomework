if __name__ == '__main__':
    r = int(input())
    c = int(input())
    r0 = int(input())
    c0 = int(input())
    sum = r * c
    i = 0
    k = 1
    tem = 0
    res = []
    res.append([r0, c0])
    i += 1
    while i < sum:
        if tem%4 ==0:
            for j in range(0,k):
                c0 += 1
                if c0 > c-1 or c0<0 or r0<0 or r0>r-1:
                    continue
                else:
                    res.append([r0,c0])
                    i+=1
            tem+=1
        elif tem%4==1:
            for j in range(0, k):
                r0 += 1
                if r0 > r-1 or r0<0 or c0<0 or c0>c-1:
                    continue
                else:
                    res.append([r0, c0])
                    i += 1
            tem+=1
            k+=1
        elif tem%4==2:
            for j in range(0,k):
                c0 -= 1
                if c0<0 or c0>c-1 or r0<0 or r0>r-1:
                    continue
                else:
                    res.append([r0,c0])
                    i+=1
            tem+=1
        elif tem % 4 == 3:
            for j in range(0, k):
                r0 -= 1
                if r0 < 0 or r0>r-1 or c0<0 or c0>c-1:
                    continue
                else:
                    res.append([r0, c0])
                    i += 1
            tem += 1
            k+=1
    print(res)