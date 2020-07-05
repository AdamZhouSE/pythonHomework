# 45
n = int(input())
for i in range(n):
    input()
    inp = input()
    num = inp.split()
    num = strsort(num)
    print('.join(num))
    
def strsort(s):
    s.sort(reverse = True)
    for i in range(len(s)):
        if i==0:
            continue
        if len(s[i-1]) > len(s[i]) and s[i-1][:len(s[i])] == s[i]:
            t = s[i]
            s[i] = s[i-1]
            s[i-1] = t
    return s