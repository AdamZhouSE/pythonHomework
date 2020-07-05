num = int(input())
for i in range(num):
    ans = []
    a, b = map(int, input().split(" "))
    m = list(map(int, input().split(" ")))
    n = list(map(int, input().split(" ")))
    for j in range(len(m)):
        if m[j] in n:
            ans.append(m[j])
    print(len(set(ans)))
