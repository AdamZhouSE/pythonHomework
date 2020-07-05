m = int(input())
for v in range(0, m):
    #a, b = map(int, input().split())
    num = int(input())
    s = list(str(bin(num))[2:])
    b = s.count('1')
    if b%2 == 0:
        print("even")
    else:
        print("odd")