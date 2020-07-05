T = int(input())

for i in range(0, T):
    temp = list(input().split(" "))
    A = int(temp[0])
    B = int(temp[1])

    if B*(B + 1) / 2 <= A:
        print(1)
    else:
        print(0)
