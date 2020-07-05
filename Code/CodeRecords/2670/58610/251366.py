for _ in range(eval(input())):
    num = eval(input())
    print(2 ** (len(bin(num)) - 2) - 1 - num)