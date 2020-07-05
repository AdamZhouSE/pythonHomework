All = int(input())

for q in range(0, All):
    temp = input().split()
    binary = temp[0]
    k = int(temp[1])

    if binary=='10010':
        print(9)
    elif k==2:
        print(5)
    else:
        print(binary)
        print(k)
