a = int(input())
for i in range(a):
    a1 = 0
    sum = 0
    b = list(input())
    for j in b:
        if j == "{" :
            a1 += 1
        elif j == "}" and a1 >0:
            a1 -= 1
        else:
            sum += 1
            a1 += 1
    if a1 %2 == 1:
        print(-1)
    else:
        print((a1>>1)+sum)