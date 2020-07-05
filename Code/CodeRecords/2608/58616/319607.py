for _ in range(int(input())):
    string = input().strip()
    n = len(string)
    ans = []
    for i in range(2 ** n):
        b = bin(i)[2:]
        b = '0' * (n - len(b)) + b
        new = ''
        for j, bit in enumerate(b):
            if bit == '1':
                new += string[j]
        if new != '':
            ans.append(new)
    ans = [ele for ele in ans if (ele[0] in 'aeiou' and ele[-1] not in 'aeiou')]
    ans = list(set(ans))
    ans.sort()
    if len(ans) == 0:
        print(-1)
    else:
        print(*ans)
    