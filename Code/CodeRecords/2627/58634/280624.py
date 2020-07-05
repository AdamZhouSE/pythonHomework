t = int(input())
for i in range(t):
    p,s = map(int,input().split(" "))
    l = (p - pow(p * p - 24 * s, 0.5)) / 12
    V = l * (s / 2 - l * (p / 4 - l))
    print("{:.5f}".format(V))