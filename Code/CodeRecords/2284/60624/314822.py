def func39():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        nums = list(map(int, input().split(" ")))
        flag = False
        for j in range(n-1,0,-1):
            for i in range(j):
                if nums[i] < nums[j]:
                    print(j-i)
                    flag = True
                    break
            if flag:
                break
    return
func39()