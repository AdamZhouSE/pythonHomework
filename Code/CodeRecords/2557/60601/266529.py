n = eval(input())
for i in range(n):
    s = input()
    re = ''
    j = 0
    i = 0
    while i<len(s):
        if i!=len(s)-1:
            re = re + s[i]
            if s[i] == s[i+1]:
                j = i + 1
                while(s[j]==s[i] and j<len(s)):
                    j = j + 1
                i = j
                continue
            else:i = i + 1
        else:
            re = re + s[i]
            i = i + 1
    print(re)


