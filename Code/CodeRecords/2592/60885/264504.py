def test():
    r = int(input())
    d = 2*r
    count = 0
    for i in range(1, d):
        for j in range(1,d):
            if i*i+j*j <= d*d:
                count += 1
    A.append(count)

A = []
for i in range(int(input())):
    test()

for i in A:
    print(i)