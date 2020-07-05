num = int(input())
for i in range(num):
    aa = input().split(" ")
    x = []
    for j in range(len(aa)):
        x.append(int(aa[j]))
    a = x[0]
    b = x[1]
    c = x[2]
    y = pow(a, b)
    print(y % c)