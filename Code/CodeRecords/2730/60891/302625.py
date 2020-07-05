t = int(input())
ans_l = []
for i in range(t):
    n = int(input())
    a_str_l = [i for i in input().split()]
    sum = 0
    for j in range(n):
        s = a_str_l[j]
        for k in range(len(s)):
            sum+=int(s[k])
    if sum%3==0:
        ans_l.append(1)
    else:
        ans_l.append(0)
for i in ans_l:
    print(i)