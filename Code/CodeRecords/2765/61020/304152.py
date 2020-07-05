import math

T = int(input())

for i in range(T):
    P = int(input())
    Tm = int(input())
    R = int(input())

    print(int(math.floor(P * Tm * R)))
