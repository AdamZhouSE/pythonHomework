for t in range(int(input())):
    for i in range(1, int(input()) + 1):
        print(bin(i)[2:], end=" ")
    print()