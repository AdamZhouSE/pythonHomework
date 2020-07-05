from itertools import permutations
def nth47Number(s):
    # a = []
    # j = 4
    # while len(a) < s:
    #     if (str(j)).count('4')+(str(j)).count('7') == len(str(j)):
    #         a.append(j)
    #     # print(a)
    #     j += 1
    # return a[s-1]
    # print(a[s])
    i = 0
    while pow(2,i) - 2 < s:
        i+=1
    i-=1
    k = s - pow(2,i)+2
    a = []
    for j in range(i+1):
        b = list(permutations([4]*(i-j)+[7]*j))
        # print(b)
        c = []
        for z in b:
            if len(a) > k:
                break
            temp = int(''.join(list(map(str,z))))
            if  not temp in c:
                c.append(int(''.join(list(map(str, z)))))
        a = a + c
    # print(sorted(a))
    # print(k)
    return sorted(a)[k-1]
    # print(sorted(a)[k])
    # a = list(permutations(list[4,4,7,7]))
    # a = sorted(a)
    # print(a[k-1])


T = int(input())
for i in range(T):
    s = int(input())
    print(nth47Number(s))