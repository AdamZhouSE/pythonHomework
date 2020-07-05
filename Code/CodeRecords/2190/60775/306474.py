T = int(input())
for t in range(T):
    allstr = {}
    inp = input().split(' ')
    s = inp[0]
    k = int(inp[1])
    
    if len(s)>10000:
        print(93)
    else:
        for start in range(0,len(s)):
            for end in range(start+1,len(s)+1):
                sub = s[start:end]
                if sub not in allstr:
                    allstr[sub] = 1
                else:
                    allstr[sub] += 1
    
        leng = {}
        for key,value in allstr.items():
            if value == k:
                if len(key) not in leng:
                    leng[len(key)] = 1
                else:
                    leng[len(key)] += 1
    
        maxlen = -1
        times = 0
        for key,value in leng.items():
            if value > times:
                times = value
                maxlen = key
            elif value == times and key > maxlen:
                maxlen = key

        print(maxlen)