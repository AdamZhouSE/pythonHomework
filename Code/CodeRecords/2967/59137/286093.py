def s17():
    def sets(items):
        result = [""]
        for i in range(len(items)):
            for j in range(i+1, len(items)+1):
                result.append(items[i:j])
        return result

    n = int(input())
    string = input()
    ans = sets(string)

    for i in range(1, n):
        string = input()
        now = sets(string)
        ans = list(set(ans).intersection(set(now)))

    l = 0
    for s in ans:
        if len(s) > l:
            l = len(s)
    print(l)


s17()