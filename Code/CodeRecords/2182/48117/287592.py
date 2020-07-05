questNum = int(input())

for quest in range(questNum):
    nk = input().split(' ')
    n = int(nk[0])
    k = int(nk[1])
    member = [_ for _ in range(1, n + 1)]

    index = 0
    while member.count(0) < n - 1:
        count = 0
        if index + k > n:
            for i in range(index, n):
                if member[i] != 0:
                    count += 1

                if count == k:
                    member[i] = 0
                    break

            for j in range(0, (index + k) % n):
                if member[j] != 0:
                    count += 1

                if count == k:
                    member[j] = 0
                    break

        else:
            for i in range(index, index + k):
                if member[i] != 0:
                    count += 1

                if count == k:
                    member[i] = 0
                    break
        end = (index + k) % n
        indexCopy = index
        while index < end:
            if member[indexCopy] != 0:
                index += 1
                indexCopy += 1
            else:
                indexCopy += 1

    for j in member:
        if j != 0:
            print(j)
            break