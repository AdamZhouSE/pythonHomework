def satisfy_feature(s):
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            return False
    return True

t = int(input())
for k in range(t):
    n = int(input())
    a = []
    for i in range(1,n+1):
        i_2 = bin(i)[2:]
        if satisfy_feature(i_2):
            a.append(str(i))
    print(' '.join(a))