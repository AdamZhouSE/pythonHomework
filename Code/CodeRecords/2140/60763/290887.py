def rotate(n):
    s = []
    t = []
    for i in range(n):
        s.append(i)
    for i in range(n):
        # print(s)
        if (i+1) % len(s) !=0:
            s = s[(i+1)%len(s):len(s)]+s[0:(i+1)%len(s)]
        t.append(s[0])
        s.remove(s[0])
    st = []
    for i in range(n):
        st.append(i)
    for j in t:
        st[j] = t.index(j)+1
    return st

T =int(input())
for i in range(T):
    N = int(input())
    # print(rotate(N))
    a = rotate(N)
    for j in range(N-1):
        print(a[j],end=' ')
    print(a[N-1])