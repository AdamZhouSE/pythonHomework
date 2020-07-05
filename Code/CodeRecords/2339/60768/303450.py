k = int(input())
for ex in range(k):
    n = int(input())
    num = [int(i) for i in input().split(' ')]
    re = 0
    for i in range(n):
        for j in range(i + 1, n):
            if num[i] > num[j]:
                re += 1
    print(re)