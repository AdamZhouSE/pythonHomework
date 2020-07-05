check = int(input())
for k in range(check):
    num = int(input())
    borads = input().split(' ')
    borads = [int(x) for x in borads]
    borads.sort()
    for i in range(1, num + 1):
        if i > borads[num - i]:
            print(i - 1)
            break
        if i == num:
            print(i)
