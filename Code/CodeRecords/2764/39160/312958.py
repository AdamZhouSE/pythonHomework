def go(n):
    if n<12:
        return n
    else:
        p=n//2
        q=n//3
        r=n//4
        return max((go(p)+go(q)+go(r)),n)
    
t=int(input())
for i in range(t):
    n=int(input())
    print(go(n))