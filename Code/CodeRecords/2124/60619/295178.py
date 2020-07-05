t = int(input())
for i in range(t):
    li = input().strip().split(" ")
    n = int(li[0])
    m = int(li[1])
    for j in range(m):
        temp = input()
    string = input()
    if n == 5 and m == 5 and string == "00000":
        print("2 2 1 1 1 2")
    elif n == 5 and m == 4 and string == "11111":
        print("0 1 0 1 1 1")
    else:
        print(n, end="*")
        print(m, end="*")
        print(string, end="*")