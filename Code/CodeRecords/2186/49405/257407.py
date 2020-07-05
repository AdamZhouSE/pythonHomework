ans = [0]
s = 1
for i in range(2, 1001):
    s += i
    ans.append(s + ans[len(ans) - 1])

T = int(input())
for t in range(T):
    print(ans[int(input()) - 1] + 1)