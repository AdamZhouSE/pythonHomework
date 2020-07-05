def s10():

    def sets(items):
        result = ['']
        for y in items:
            result.extend([subset + y for subset in result])
        return result

    t = int(input())
    for x in range(t):
        string = input()
        sub = sets(string)
        sub.pop(0)

        ans = []
        for s in sub:
            if s[0] in "aeiou" and s[-1] not in "aeiou":
                ans.append(s)
        ans = list(sorted(set(ans)))

        if len(ans) == 0:
            print(-1)
        else:
            for i in range(len(ans)-1):
                print(ans[i], end=" ")
            print(ans[-1])

            
s10()