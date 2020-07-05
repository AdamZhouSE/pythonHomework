def test():
    s,t,l,r = list(map(int, input().split()))
    a = A[s-1:t]
    b = B[l-1:r]
    ans = 0
    start = 0
    while start < len(a)-len(b)+1:
        temp = a[start:start+len(b)]
        if temp == b:
            ans += K - start - s
            start += len(b)
        else:
            start += 1
    return ans

n,K = list(map(int, input().split()))
A = input()
B = input()

result = []
for i in range(int(input())):
    result.append(test())

for i in result:
    print(i)