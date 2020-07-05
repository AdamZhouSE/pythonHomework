T =int(input())
for i in range(T):
    st = (''+input()).split(' ')
    s = st[0]
    t = int(st[1])
    count = 0
    for j in range(len(s)):
        for k in range(j+1,len(s)+1):
            if s[j:k].count('1') == t:
                count+=1
    print(count)