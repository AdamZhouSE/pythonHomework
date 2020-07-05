def func(n : list) -> int :
    MAX_LENGTH = 0
    for i in range(len(n)):
        cnt = 1
        tmp = int(n[i])
        for j in range(i+1,len(n)):
            if int(n[j]) > tmp :
                tmp = int(n[j])
                cnt += 1
        if cnt > MAX_LENGTH :
            MAX_LENGTH = cnt
    return MAX_LENGTH

n = input().split(",")
print(func(n))
