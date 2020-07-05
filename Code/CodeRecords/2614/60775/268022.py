

test = int(input())
for i in range(test):
    length = int(input())
    A = [int(x) for x in input().split(' ')]
    B = [int(x) for x in input().split(' ')]
    C = [int(x) for x in input().split(' ')]
    count = 0
    for j in range(length):
        if A[j]-B[j] in C:
            count += 1
    print(count)