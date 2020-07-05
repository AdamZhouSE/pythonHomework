inp = input().split(',')
target = int(input())
tmp = [int(inp[i]) for i in range(len(inp))]
n = len(tmp)
if tmp[n - 1] == target:
    print(n - 1)
elif tmp[n - 1] < target:
    print(n)
elif tmp[0] > target:
    print(0)
else:
    for i in range(0, n - 1):
        if tmp[i] == target:
            print(i)
            break
        elif (tmp[i] < target) & (tmp[i + 1] > target):
            print(i + 1)
            break
        else:
            continue
