src=input()
sub=[]
for i in range(len(src)):
    sub.append(src[:i+1])
for s in sub:
    n=len(s)
    if n==1:
        print(0)
        continue
    ans=0
    for i in range(n-1):
        for j in range(i+1, n):
            for l in range(1, n-j+1):
                if j <= i+l-1:
                    ans += l if s[i:i+l] == s[j:j+l] else 0
    print(ans % (10**9+7))
