for t in range(int(input())):
    print("1", end="")
    for i in range(2, int(input()) + 1):
        print(" " + bin(i)[2:], end="")
    print()