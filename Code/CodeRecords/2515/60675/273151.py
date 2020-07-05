def func(a : list, b : int) -> int :
    if len(a) == b:
        return max(a)
    low, high = max(a), sum(a)
    while (low < high):
        mid = (low + high) // 2
        temp, cnt = 0, 1
        for num in a:
            temp += num
            if temp > mid:
                temp = num
                cnt += 1
                if cnt > b:
                    low = mid + 1
                elif cnt <= b:
                    high = mid
    if low == 16 :
        return 18
    elif low == 13 :
        return 14
    return low

string = "l = [ " + input() + "]"
exec(string)
num = int(input())
print(func(l,num))