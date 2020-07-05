def f(n):
    s=[0]*n
    for i in range(1,n+1):
        start=-1
        while start<n-i:
            start+=i
            s[start]=1-s[start]
    return s.count(1)

print(f(int(input().strip())))