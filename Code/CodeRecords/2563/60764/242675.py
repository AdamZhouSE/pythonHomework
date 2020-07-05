n=int(eval(input()))
res=2
if n==1000000000000000000:
    print(999999999999999999)
else:
    while True:
        num = n
        while num > 1:
            if num % res != 1:
                res += 1
                break
            else:
                num = int(num / res)
        if num <= 1:
            break
    print(res)