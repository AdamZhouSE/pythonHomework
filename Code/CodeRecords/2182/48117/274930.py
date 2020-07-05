questNum = int(input())

for quest in range(questNum):
    nk = input().split(' ')
    n = int(nk[0])
    k = int(nk[1])
    member = [_ for _ in range(1, n + 1)]

    index = -1
    while len(member) > 1:
        index = (index + k) % n
        del member[index]
    
    print(member[0])