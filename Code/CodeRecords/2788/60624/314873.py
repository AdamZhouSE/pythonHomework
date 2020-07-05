def func30():
    b = int(input())
    boys = list(map(int, input().split(" ")))
    g = int(input())
    girls = list(map(int, input().split(" ")))
    boys.sort()
    girls.sort()
    i = 0
    j = 0
    ans = 0
    while i<b and j<g:
        if abs(boys[i]-girls[j]) <= 1:
            i += 1
            j += 1
            ans += 1
        elif boys[i]-girls[j] > 1:
            j += 1
        elif girls[j]-boys[i] > 1:
            i += 1
    print(ans)
    return
func30()