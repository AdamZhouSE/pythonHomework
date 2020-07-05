#03
#算术级数：等差数列
T = int(input())
for i in range(0,T):
    ori = input().split(" ")
    A = int(ori[0])
    B = int(ori[1])
    N = int(input())
    d = B - A
    outcome = A + (N-1)*d
    print(outcome)