m = int(input())
for v in range(0, m):
    a, b = map(int, input().split())
    #num = int(input())
    ls = list(int(n) for n in input().split(' '))
    ans = []
    for i in ls:
        if i % b == 0 and i != b:
            ans.append(i)
    print(sum(ans))