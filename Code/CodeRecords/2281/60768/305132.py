k = int(input())
for e in range(k):
    n = int(input())
    num = [int(i) for i in input().split(' ')]
    re = []
    for i in range(len(num)):
        for j in range(i, len(num)):
            if num[i] < num[j]:
                break
        else:
            re.append(num[i])
    re = [str(i) for i in re]
    print(' '.join(re))
