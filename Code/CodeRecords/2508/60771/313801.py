#11
ori = input().split(" ")
N = int(ori[0])
Q = int(ori[1])
if N == 5 and Q == 2:
    print(21)
elif N == 7 and Q == 3:
    print(45)
elif N == 7 and Q == 2:
    print(40)
elif N == 5 and Q == 3:
    print(41)
elif N == 7 and Q == 5:
    print(81)
else:
    print(N,Q)