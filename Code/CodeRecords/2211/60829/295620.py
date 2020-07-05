n, k = [int(i) for i in input().split(' ')]
fromwho = {}
number = {}
fromw = {}
for i in range(1, n+1):
    s, t = input().split(' ')
    number[i] = s
    t = int(t)
    fromw[i] = t
    if s in fromwho.keys():
        fromwho[s].append(t)
    else:
        fromwho[s] = [t]
for i in range(k):
    s = input()
    n = len(s)
    nums = temp = 0
    if s[0] in fromwho.keys():
        temp = set(fromwho[s[0]])
        nums = len(temp)
        j = 1
        while j < n:
            for i in temp.copy():
                temp.remove(i)
                if i == 0 or number[i] != s[j]:
                    nums -= 1
                else:
                    temp.add(fromw[i])
            j += 1
    print(nums)