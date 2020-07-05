from math import sqrt

T = int(input())
examples=[]
for i in range(0, T):
    examples.append(input().split(" "))
for i in range(0, T):
    l = (float(examples[i][0]) - sqrt(float(examples[i][0]) * float(examples[i][0]) - 24 * float(examples[i][1]))) / 12
    V = l * (float(examples[i][1]) / 2.0 - l * (float(examples[i][0]) / 4.0 - l))
    print("%.5f"%V)