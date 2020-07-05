T = int(input())
while T > 0:
    T -= 1
    length = int(input())
    inp = input().split(' ')
    nstr = [int(inp[i]) for i in range(len(inp))]
    # print(nstr)

    res = 0
    for i in range(0, length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                if (int(inp[i]) + int(inp[j]) <= int(inp[k])) | (int(inp[i]) + int(inp[k]) <= int(inp[j])) | (
                        int(inp[j]) + int(inp[k]) <= int(inp[i])):
                    continue
                else:
                    res += 1
    print(res)
