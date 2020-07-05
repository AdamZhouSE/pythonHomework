import math
num=int(input())
for i in range(num):
    P,A=input().split(' ')
    P,A=int(P),int(A)

    l = (float)(P - math.sqrt(P * P - 24 * A)) / 12;

    V = (float)(l * (A / 2.0 - l * (P / 4.0 - l)));
    print("%.4f"%V);