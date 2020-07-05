def nth47Number(s):
    a = []
    j = 4
    while len(a) < s:
        if (str(j)).count('4')+(str(j)).count('7') == len(str(j)):
            a.append(j)
        # print(a)
        j += 1
    return a[s-1]
    # print(a[s])
    # i = 0
    # while pow(2,i) - 2 <= s:
    #     i+=1
    # i-=1
    # k = s - pow(2,i)+2
    # for j in range(,)
    # a = list(permutations(list[4,4,7,7]))
    # a = sorted(a)
    # print(a[k-1])


T = int(input())
for i in range(T):
    s = int(input())
    print(nth47Number(s))