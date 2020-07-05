
T = int(input())
for t in range(T):
    string = input().split(' ')
    binary = string[0]
    k = int(string[1])
    all = []
    result = 0
    for start in range(len(binary)):
        end = start
        has1 = 0
        while end < len(binary) and has1 <= k:
            tmp = binary[start:end+1]
            if binary[end] == '1':
                has1 += 1
            if binary[end] == '1' and has1 > k:
                break
            if has1 == k :#and tmp not in all:
                all.append(tmp)
                result += 1
            end += 1
    print(result)


