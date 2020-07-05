num = int(input())
for i in range(num):
    aa = input().split(" ")
    n = int(aa[0])
    m = int(aa[1])
    if n % 2 != 0:
        x = n // 2 + 1
        print(x*m)
    else:
        print(int(n*m/2))