n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(n):
    ans.append(sum(a[:i+1]) - sum(a[i+1:]))
if len(a) == 1:
    print(a[0])
    quit()
print(max(ans)) 