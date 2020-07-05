t = int(input())
for x in range(t):
    n = input()
    nums = input().split()
    count0 = 0
    count1 = 0
    count2 = 0
    for y in nums:
        if int(y) % 3 == 0:
            count0 += 1
        elif int(y) % 3 == 1:
            count1 += 1
        elif int(y) % 3 == 2:
            count2 += 1
    print(count0 + min(count1, count2))
