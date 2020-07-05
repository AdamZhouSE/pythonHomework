t = int(input())
for i in range(0,t):
    s = input().lower()
    sRe = ''.join(reversed(s))
    length = -1
    for j in range(0,len(s)):
        if(s.count(s[j]) > 1):
            index = sRe.index(s[j])
            if(len(s) - index - j - 2 > length):
                length = len(s) - 2 - index - j    
    print(length)