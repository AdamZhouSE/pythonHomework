def permutation(s_list, start, last):
    if start >= last:
        sets.append("".join(s_list))
    else:
        for i in range(start, last):
            s_list[i], s_list[start] = s_list[start], s_list[i]
            permutation(s_list, start + 1, last)
            s_list[i], s_list[start] = s_list[start], s_list[i]


message = input()
n = int(input())
sum = 0
for i in range(0, n):
    sets = []
    key = input()
    permutation(list(key), 0, len(key))
    sets=list(set(sets))
    for j in sets:
        sum += message.count(j)
print(sum)