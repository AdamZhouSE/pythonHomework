def bala(s1,s2):
    s = set(s2)
    for l in range(len(s2), len(s1) + 1):
        for i in range(len(s1) - l + 1):
            if set(s1[i:i + l]) & s == s:
                return s1[i:i+l]
    else:
        return -1

t = int(input())
for j in range(t):
    s1=input()
    s2=input()
    print(bala(s1,s2))