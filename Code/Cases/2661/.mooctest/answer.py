for t in range(int(input())):
    b = bin(int(input()))[2:]
    print(b.count('1')^b.count('0'))
    