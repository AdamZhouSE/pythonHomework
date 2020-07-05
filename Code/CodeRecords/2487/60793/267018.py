from collections import Counter
for test in range(0, int(input())):
    input()
    names = Counter(list(input().split()))
    sorted(names.items(), key=lambda item:item[1], reverse=True)
    ls1, ls2 = [], []
    for i in names.items():
        ls1.append(i[0])
        ls2.append(i[1])
    result = [ls1[0], ls2[0]]
    for i in range(1, len(ls1)):
        if ls2[i] > result[-1]:
            result[0], result[-1] = ls1[i], ls2[i]
        elif ls2[i] == result[-1] and ls1[i] < result[0]:
            result[0], result[-1] = ls1[i], ls2[i]
    print(result[0], result[-1])