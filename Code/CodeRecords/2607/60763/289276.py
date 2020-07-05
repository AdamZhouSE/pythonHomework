def isEqual(s):
    return s.count('0') == s.count('1') and s.count('1') == s.count('2')

T = int(input())
for i in range(T):
    s = ''+input()
    # print(s)
    count = 0
    for j in range(len(s)):
        for k in range(j+1,len(s)+1):
            # print(s[j:k])
            if s[j:k].count('0') == s[j:k].count('1') and s[j:k].count('1') == s[j:k].count('2'):
                count+=1
    print(count)