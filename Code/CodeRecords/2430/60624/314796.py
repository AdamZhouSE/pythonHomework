def func46():

    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        nums = list(map(int, input().split(" ")))
        k = int(input())
        temp = list(set(nums))
        low, high = 0, len(temp)-1
        flag = True
        while high > low:
            if temp[low]+temp[high] == k:
                print(str(temp[low])+" "+str(temp[high])+" "+str(k))
                flag = False
            if temp[high] > k or temp[high]+temp[low] > k:
                high -= 1
            else:
                high -= 1
                low += 1
        if flag:
            print(-1)
    return
func46()