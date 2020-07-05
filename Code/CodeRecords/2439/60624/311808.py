def func7():
    n = int(input())
    temp = []
    for i in range(n-1):
        a = list(map(int, input().split(" ")))
        temp.append(a)
    m = int(input())
    ans = []
    for i in range(m):
        a = list(map(int, input().split(" ")))
        res = 0
        if a[0] == a[1]:
            ans.append(res)
        else:
            def helper(a:int, b:list):
                for i in range(len(b)):
                    if b[i][0] == a:
                        return b[i]
            k = []
            t = a[0]
            cur = helper(t,temp)
            while cur[1] != a[1]:
                k.append(cur[2])
                t = cur[1]
                cur = helper(t,temp)
            k.append(cur[2])
            res = k[0]
            for i in range(1,len(k)):
                res = res ^ k[i]
            ans.append(res)
    for i in ans:
        print(i)
func7()