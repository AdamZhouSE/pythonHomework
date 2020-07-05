ucnum = int(input())
ans = list()
wordlist = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
for i in range(ucnum):
    strs = input()
    lists = list(strs)
    maxlen = 0
    for j in range(len(lists)):
        lens = 0
        for k in range(j+1,len(lists)):
            if wordlist.index(lists[k])>wordlist.index(lists[k-1]):
                lens+=1
            else:
                break
        if lens>maxlen: maxlen = lens
    ans.append(maxlen)
for i in ans:
    print(i)