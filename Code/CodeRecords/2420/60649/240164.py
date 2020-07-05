n=int(input())
for i in range(n):
    k=n-i
    if '0' in str(k) or '0' in str(i):
        continue
    else:
        print([i,k])
        break
