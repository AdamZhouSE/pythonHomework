num=int(input())
if num==0:
    print(False)
else:
    jud = True
    while num != 1:
        if num % 3 != 0:
            jud = False
            break
        num = num // 3
    print(jud)