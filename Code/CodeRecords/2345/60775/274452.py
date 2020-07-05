T = int(input())

for t in range(T):
    size = int(input())
    nums = [int(x) for x in input().split(' ')]
    A = 0
    B = 0
    foundA = False
    foundB = False

    occur = [0 for i in range(size)]
    for x in nums:
        occur[x-1] += 1
    for i,n in enumerate(occur):
        if n == 0 and foundA == False:
            foundA = True
            A = i + 1
        elif n > 1 and foundB == False:
            foundB = True
            B = i + 1
        elif foundA and foundB:
            break
    print(B,A)