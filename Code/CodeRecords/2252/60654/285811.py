a = int(input())
for i in range(a):
    b = list(input())
    c = list(input())
    sum = 0
    sign = True
    while True:
        for k in range(c.__len__()):
            if c[k] in b:
                b.remove(c[k])
            else:
                sign = False
                break
            if k == c.__len__()-1:
                sum += 1
                break
        if not sign :
            break
    print(sum)