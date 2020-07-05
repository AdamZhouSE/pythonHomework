T = int(input())
for i in range(T):
    N = int(input())
    nums = [int(i) for i in input().split(' ')]
    temp = []
    for i in nums:
        if i % 2 == 0:
            print(i, end=' ')
        else:
            temp.append(i)
    for i in temp:
        print(i, end=' ')
    print()