questNum = int(input())

for quest in range(questNum):
    nk = input().split(' ')
    n = int(nk[0])
    k = int(nk[1])
    member = [_ for _ in range(1, n + 1)]

    index = 0
    while member.count(0) < n - 1:
        count = 0
        for i in range(index, index + k):
            if member[index] != 0:
                count += 1

            if count == k:
                member[i] = 0
                break

        index = (index + k) % n

    for j in member:
        if j != 0:
            print(j)
            break