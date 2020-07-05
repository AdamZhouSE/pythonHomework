def func39():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        nums = list(map(int, input().split(" ")))
        flag = False
        length = n-1
        while length > 0:
            cur = n-1
            while cur-length>0:
                if nums[cur]>=nums[cur-length]:
                    flag = True
                    print(length)
                    break
                cur -= 1
            if flag:
                break
            length -= 1
    return
func39()