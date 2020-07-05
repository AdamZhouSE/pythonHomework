All = int(input())

for q in range(0, All):
    s = input()
    num = len(s)
    k = int(input())

    longest = 0
    dic = {}
    index = 0
    i = 0
    while index < num:
        while index < num and len(dic) <= k:
            c = s[index]
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
            index += 1
        if index - i > longest:
            longest = index - i

        c = s[i]
        while dic[c] > 1:
            dic[c] -= 1
            i += 1
            c = s[i]
        del dic[c]
        i += 1
    print(longest)
