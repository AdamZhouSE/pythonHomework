T = int(input())
for i in range(0, T):
    first = [int(x) for x in input().split()]
    second = [int(x) for x in input().split()]
    if first[0] < second[0] < first[2] and first[3] < second[1] < first[1] or \
            first[0] < second[0] <= first[2] and first[3] < second[3] < first[1] or \
            first[0] < second[2] < first[2] and first[3] < second[1] < first[1] or \
            first[0] < second[2] < first[2] and first[3] < second[3] < first[1]:
        print(1)
    else:
        print(0)
