n_m = input().split(" ")
n = int(n_m[0])
m = int(n_m[1])
letters, ans = [], []
for i in range(n):
    letters.append(input())
for j in range(m):
    t = input().split(" ")
    f = int(t[0]) - 1
    l = int(t[1])
    temp = letters[f:l]
    temp.sort()
    ans.append(temp[len(temp) - 1])
for x in ans:
    print(x)
