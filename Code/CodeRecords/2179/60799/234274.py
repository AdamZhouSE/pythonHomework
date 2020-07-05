
m = int(input().split(' ')[1])
s = input()

for i in range(0, m):
    list = [int(i) for i in input().split(' ')]
    j = 0

    while j < min(list[1]+1-list[0], list[3]+1-list[2]):
        if s[list[0]+j] == s[list[2]+j]:
            j += 1
        else:
            break
    print(j)
