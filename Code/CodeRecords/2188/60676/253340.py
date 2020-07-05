def cover_substring(k, str1, str2, s, t, l, r):
    obj = str2[l-1:r]
    index = s-1
    res = 0
    while index < t-r+l:
        if str1[index:index+r-l+1] == obj:
            res += k-index-1
            index += r-l+1
            continue
        index += 1
    return res


K = int(input().split()[-1])
stringA = input()
stringB = input()
result = []
for i in range(eval(input())):
    indexes = input().split()
    for j in range(len(indexes)):
        indexes[j] = int(indexes[j])
    result.append(cover_substring(K, stringA, stringB, indexes[0], indexes[1], indexes[2], indexes[3]))
for i in range(len(result)):
    print(result[i])