def s11():
    t = int(input())
    for i in range(t):
        string = input()
        ans = -1
        for s in string:
            if string.count(s) > 1:
                index1 = string.find(s)
                index2 = string.rfind(s)
                if index2 - index1 - 1 > ans:
                    ans = index2 - index1 - 1
        print(ans)


s11()