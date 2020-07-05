n, t = input().split(' ')
n = int(n)
t = int(t)
nums = input().rstrip().split(' ')
# print(nums)
num = [int(nums[i]) for i in range(len(nums))]
for i in range(t):
    inp = input().split(' ')
    if inp[0] == '1':
        x = int(inp[1]) - 1
        y = int(inp[2])
        tmp = num[x:y]
        for j in range(len(tmp)):
            if tmp[j] == int(inp[3]):
                print(7)
                break
    elif inp[0] == '2':
        x = int(inp[1]) - 1
        y = int(inp[2])
        tmp = num[x:y]
        index = int(inp[3]) - 1
        print(tmp[index])
    elif inp[0] == '3':
        index = int(inp[1]) - 1
        num[index] = int(inp[2])
    elif inp[0] == '4':
        x = int(inp[1]) - 1
        y = int(inp[2])
        tmp = num[x:y]
        tmp.sort()
        for j in range(1, len(tmp)):
            if tmp[j - 1] < int(inp[3]) and tmp[j] > int(inp[3]):
                print(tmp[j - 1])
                break
    else:
        x = int(inp[1]) - 1
        y = int(inp[2])
        tmp = num[x:y]
        tmp.sort()
        for j in range(1, len(tmp)):
            if tmp[j]>int(inp[3]):
                print(tmp[j])
                break

