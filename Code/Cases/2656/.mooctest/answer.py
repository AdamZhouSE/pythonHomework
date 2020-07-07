T = int(input())
for i in range(T):
    L = [int(n) for n in input().strip().split()]
    num1 = format(L[0], 'b').zfill(12)
    num2 = format(L[1], 'b').zfill(12)
    for j in range(-1, -12, -1):
        if(num1[j] != num2[j]):
            print(abs(j))
            break