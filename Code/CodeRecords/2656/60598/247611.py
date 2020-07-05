times = int(input())
for i in range(times):
    cin = input().split()
    num1 = int(cin[0])
    num2 = int(cin[1])
    binary = str(bin(num1 ^ num2))
    check = False
    for j in range(len(binary)):
        if binary[len(binary)- j -1] == "1":
            check = True
            print(j+1)
            break
    if not check:
        print(-1)
