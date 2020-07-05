def longConsist(n: int) -> int:
    s = str(bin(n))[2:]
    l = list(map(int, s))
    MAX_LEN, cnt = 0, 0
    isCount = False
    for i in range(len(l)):
        cnt += 1
        if l[i] == 1 and isCount == False:
            cnt = 0
            isCount = True
        elif l[i] == 1 and isCount == True :
            isCount = False
            if cnt > MAX_LEN :
                MAX_LEN = cnt
            cnt = 0
    return  MAX_LEN

n = int(input())
print(longConsist(n))