def f(s,t):
    m=0
    for i in range(1,len(s)+1):
        for j in range(0,len(s)-i+1):
            m+=t.count(s[j:j+i])
    return m

print(f(input().strip(),input().strip()),end='')