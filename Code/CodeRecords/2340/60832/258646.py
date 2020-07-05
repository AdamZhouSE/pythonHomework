All = int(input())

for q in range(0, All):
    length = int(input())
    box = list(map(int, input().split()))
    ans = 0

    if box[0] <= box[length - 1]:
        big = length - 1
        small = 0
        index = small + 1
    else:
        big = 0
        small = length - 1
        index = small - 1

    while index != small and index != big:
        if big > small:
            if box[small] >= box[index]:
                ans += box[small] - box[index]
                index += 1
            else:
                if box[index] > box[big]:
                    small = big
                    big = index
                    index = small - 1
                else:
                    small = index
                    index += 1
        else:
            if box[small] >= box[index]:
                ans += box[small] - box[index]
                index -= 1
            else:
                if box[index] > box[big]:
                    small = big
                    big = index
                    index = small + 1
                else:
                    small = index
                    index -= 1

    print(ans)
