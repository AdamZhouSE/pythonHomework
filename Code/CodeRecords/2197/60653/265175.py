m = int(input())
for v in range(0, m):
    #l, r = map(int, input().split())
    num = int(input())
    ans = 0
    ls = list(int(n) for n in range(1, num+1))
    index = 0
    while len(ls) > 1:
        ls.remove(ls[index+1])
        index += 1
        if index+1 >= len(ls):
            index -= len(ls)
    ans = ls[0]
    print(ans)