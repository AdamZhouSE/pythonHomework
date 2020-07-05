# 16
def test():
    arr = eval(input())
    length = 1
    max_len = 1
    if len(arr) <= 1:
        print(len(arr))
        return
    if len(arr) == 2:
        if arr[1] - arr[0] <= 0:
            print(1)
        else:
            print(2)
        return
    else:
        for i in range(1, len(arr)):
            ok = False
            if arr[i] - arr[i - 1] > 0:
                if length == 1:
                    ok = True
                else:
                    if arr[i] - arr[i - 1] == arr[i - 1] - arr[i - 2]:
                        ok = True
            if ok:
                length = length + 1
            else:
                max_len = max(max_len, length)
                length = 1

        print(max_len)
test()

