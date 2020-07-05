def haveCommomFactor():
    if a > b:
        c = b
    if a < b:
        c = a
    for k in range(2, c + 1):
        if a % k == 0 and b % k == 0:
            return True
    return False


ls = input().split(",")
ls = [int(x) for x in ls]
donthave = []  # 各个数字没有公因数的
result = 0
for i in range(len(ls)):
    a = ls[i]
    this = []
    for j in range(len(ls)):
        if j != i:
            b = ls[j]
            if not haveCommomFactor():
                this.append(j)

    donthave.append(this)
for i in range(len(donthave)):
    j=0
    while j<len(donthave[i]):
        a = donthave[i][j]
        liantong=False
        for k in range(len(donthave)):
            if not donthave[i].__contains__(k):
                if not donthave[k].__contains__(a):
                    liantong=True
                    break
        if liantong:
            del donthave[i][j]
            j=j-1
        j=j+1
r=10000
for i in range(len(donthave)):
    n=len(donthave[i])
    if n<r:
        r=n

result=len(ls)-r

print(result)





