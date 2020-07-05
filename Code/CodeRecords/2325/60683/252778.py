from collections import defaultdict

cards = [int(x) for x in input().split(',')]
dic = defaultdict(int)
for i in range(len(cards)):
    dic[cards[i]] += 1
tempMin = 10001
for i in dic.items():
    # print(i[1])
    if i[1] == 1:
        print(False)
        exit()
    elif tempMin > i[1]:
        tempMin = i[1]
for i in dic.items():
    # print(i[1])
    if i[1] % tempMin != 0:
        print(False)
        exit()
print(True)