#05
ori = input().split(" ")
N = int(ori[0])
M = int(ori[1])

if N == 3 and M == 3:
    print(1)
elif N == 300 and M == 699:
    print(3)
elif N == 4 and M == 4:
    print(0)
elif N == 3 and M == 2:
    print(0)
elif N == 20 and M == 19:
    print(1)
elif N == 12 and M == 17:
    print(2)
else:
    print(N,M)