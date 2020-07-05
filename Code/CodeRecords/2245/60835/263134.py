n = int(input()) 
binary = []
one_cnt = 0
while n > 0:
    binary.append(n % 2)
    if n % 2 == 1:
        one_cnt = one_cnt + 1
    n = n // 2
max_dis = 0
cnt = 0

if one_cnt < 2:
    print(max_dis)
else:
    for x in binary:
        if x == 1 and cnt != 0:
            if max_dis < cnt:
                max_dis = cnt
            cnt = 1
        elif x == 1:
            cnt = 1
        elif cnt != 0:
            cnt = cnt + 1
    print(max_dis)
        