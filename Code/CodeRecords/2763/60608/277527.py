
def mANDn(n: int, m: int, val: list, ans: list):
    if len(val) == n:
        ans[0] += 1
    else:
        for i in range(val[-1] * 2, m + 1):
            if i > 0:
                val.append(i)
                mANDn(n, m, val, ans)
                del val[-1]



def func14():
    for _ in range(0, eval(input())):
        arr = list(map(int, input().split()))
        m, n, ans = arr[0], arr[1], [0]
        if n != 0 and m < 1:
            print(0)
        else:
            mANDn(n + 1, m, [0], ans)
        print(ans[0])


func14()

