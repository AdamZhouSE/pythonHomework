def func4():
    n = eval(input())
    res = list(map(int, input().split()))
    if len(res) == 1:
        print("YES")
    else:
        flag = 0
        ans = "YES"
        for i in range(1, n):
            if res[i] > res[i - 1]:
                if flag == 0:
                    continue
                else:
                    ans = "NO"
                    break
            elif res[i] == res[i - 1]:
                if flag == 0:
                    flag = 1
                elif flag == 1:
                    continue
                else:
                    ans = "NO"
                    break
            else:
                if flag == 1 or flag==0:
                    flag = 2
                elif flag == 2:
                    continue
                else:
                    ans = "NO"
                    break
        print(ans)


func4()
