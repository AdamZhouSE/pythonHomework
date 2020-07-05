t = int(input())
for ind in range(t):
    li = input().split(" ")
    num = int(li[0])
    k = int(li[1])
    death = []
    for i in range(num):
        death.append(1)
    escapePeople = 0
    posi = 0
    while death.count(1) > 1:
        if escapePeople == k - 1 and death[posi] == 1:
            death[posi] = 0
            escapePeople = 0
            posi = (posi+1) % num
        if death[posi] == 0:
            posi = (posi+1) % num
        if escapePeople < k-1 and death[posi] == 1:
            escapePeople += 1
            posi = (posi+1) % num
    result = death.index(1)+1
    print(result)