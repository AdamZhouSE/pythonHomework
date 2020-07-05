def func41():
    n = int(input())
    nums = list(map(int, input().split(" ")))
    flag = False
    def helper(a: int, b: int, c: int)->bool:
        if a+b>c and a+c>b and b+c>a:
            return True
        else:
            return False
    for i in range(n-2):
        if flag:
            break
        for j in range(i+1, n-1):
            if flag:
                break
            for k in range(j+1, n):
                if helper(nums[i], nums[j], nums[k]):
                    flag = True
                    break
    if flag:
        print("YES")
    else:
        print("NO")

    return
func41()