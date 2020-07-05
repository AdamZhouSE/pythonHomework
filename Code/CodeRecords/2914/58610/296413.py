for _ in range(0, eval(input())):
    n = eval(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    flag = 0
    ans = True
    bia = 0
    for i in range(0, n):
        if arr1[i] == arr2[i]:
            if flag == 1:
                flag = 2
        else:
            if flag == 2:
                ans = False
                break
            elif flag == 1:
                if arr1[i] - arr2[i] != bia:
                    ans = False
                    break
            else:
                bia = arr1[i] - arr2[i]
                if bia > 0:
                    ans = False
                    break
                flag = 1
    if ans:
        print("YES")
    else:
        print("NO")