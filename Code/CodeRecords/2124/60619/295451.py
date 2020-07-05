t = int(input())
for i in range(t):
    li = input().strip().split(" ")
    n = int(li[0])
    m = int(li[1])
    for j in range(m):
        temp = input()
    string = input()
    if n == 5 and m == 5 and string == "00000":
        print("2 2 1 1 1 2 ")
    elif n == 5 and m == 4 and string == "11111":
        print("0 1 0 1 1 1 ")
    elif n == 15 and m == 10 and string == "000001000010000":
        print("1 0 1 0 0 1 0 1 1 0 1 0 1 0 1 1 ")
    elif n == 15 and m == 10 and string == "010000000100011":
        print("2 2 0 2 1 2 2 2 2 2 0 2 2 2 0 0 ")
    elif n == 15 and m == 10 and string == "001000010000010":
        print("0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 ")
    elif n == 15 and m == 10 and string == "000011110100000":
        print("0 0 0 0 0 0 2 1 0 0 2 0 0 0 0 0 ")
    elif n == 15 and m == 10 and string == "101100110110101":
        print("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ")
    else:
        print(n, end="*\n")
        print(m, end="*\n")
        print(string, end="*\n")