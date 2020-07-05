def judge(s, t):
    c = s[0]
    if t[0] == c:
        s1, s2, t1, t2 = [], [], [], []
        for i in range(1, len(s)):
            if s[i] > c:
                s1.append(s[i])
            else:
                s2.append(s[i])
            if t[i] > c:
                t1.append(t[i])
            else:
                t2.append(t[i])
        label1 = label2 = False
        if len(t1) == len(s1):
            if t1:
                label1 = judge(s1, t1)
            else:
                label1 = True
        if len(t2) == len(s2):
            if t2:
                label2 = judge(s2, t2)
            else:
                label2 = True
        return label1 and label2
    return False


n = int(input())
while n != 0:
    s = list(input())
    length = len(s)
    for i in range(n):
        t = list(input())
        if judge(s, t):
            print('YES')
        else:
            print('NO')
    n = int(input())