def rec_res(n):
    ans = 0
    if n==0 or n==1:
        return 1
    for i in range(n):
        ans+=rec_res(i)*rec_res(n-i-1)
    return ans    
t = int(input())
for _ in range(t):
    n = int(input())
    print(rec_res(n//2))