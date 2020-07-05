num = int(input())
all = []
for i in range(num):
    n = input()
    all.append(input().split(" "))
for i in all:
    for k in range(len(i)):
        i[k] = int(i[k])
    odd = []
    notodd = []
    for k in i:
        if k%2 == 0:
            notodd.append(k)
        else:
            odd.append(k)
    odd.sort(reverse = True)
    notodd.sort()
    res = odd+notodd
    result = ""
    for i in res:
        result = result + str(i)+" "
    print(result)