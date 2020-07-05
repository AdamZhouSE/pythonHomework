t = int(input())
for i in range(t):
    inp = input().split(" ")
    N, K = int(inp[0]), int(inp[1])
    money = [int(x) for x in input().split(" ")]
    money.sort()
    count = 0
    for cost in money:
        K -= cost
        if K > 0:
            count += 1
        else:
            break
    print(count)
