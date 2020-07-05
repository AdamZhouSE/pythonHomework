s=input()
k=int(input())
ns = len(s)
ans=0
if ns <= k+1 or ns<2:
    ans=ns
else:
    start = 0
    maxlen = k+1
    change = k
    chdict = {}
    max_n = 0
    max_ch =""
    for end in range(0, ns):
        chdict[s[end]] = chdict.get(s[end],0)+1
        if chdict[s[end]] >max_n:
            max_ch = s[end]
            max_n = chdict[s[end]]
        change = end-start+1 - max_n
        while change > k:
            chdict[s[start]] -= 1
            for kv in chdict.items(): 
                if kv[1]>chdict[max_ch]:
                    max_ch = kv[0]
                    max_n = kv[1]
                    break
            start += 1
            change = (end-start+1) - max_n
        if end-start+1>maxlen:
            maxlen = end-start+1
    ans=maxlen
print(ans)