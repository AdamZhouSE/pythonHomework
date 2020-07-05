import bisect
def strtoInt(string:str) ->int:
    return int(string)

def func(n:int, m: list) -> str:
    m.sort()
    cnt = 0
    for i in range(1, n+1):
        if bisect.bisect_left(m,i) != len(m):
            cnt = i
            m.remove(m[bisect.bisect_left(m,i)])
        else:
            break
    return cnt


l = []
n = int(input())
m = list(map(strtoInt, input().split(" ")))
print(func(n,m))