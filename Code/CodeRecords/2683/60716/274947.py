import itertools
ucnum = int(input())
ans = list()
wordlist = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
for i in range(ucnum):
    strs = input()
    lists = list(strs)
    maxlen = 0
    for j in range(len(lists)):
        for temp in itertools.combinations(lists,len(lists)-j):
            check = True
            for k in range(1,len(temp)):
                if wordlist.index(temp[k])<=wordlist.index(temp[k-1]):
                    check = False
                    break
            if check :
                maxlen = len(lists)-j
                break
        ans.append(maxlen)
for i in ans:
    print(i)
