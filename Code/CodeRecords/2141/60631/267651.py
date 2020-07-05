t = int(input())
for ti in range(t):
    a=int(input())
    for i in range(1,a+1):
        print(bin(i)[2:],end=' ')
    print()