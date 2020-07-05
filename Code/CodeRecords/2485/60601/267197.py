n = eval(input())
for i in range(n):
    m = input()
    s = input().split(' ')
    for j in range(len(s)):
        s[j] = sorted(s[j])
    st = []
    for j in s:
        if j not in st:
            st.append(j)
    re = []
    for i in st:
        re.append(s.count(i))
    re.sort()
    print(' '.join(map(str,re)))