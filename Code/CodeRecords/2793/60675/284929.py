def strtoInt(string:str)-> int:
    return int(string)

def func(l: list, c:int) -> int:
    if c == 0:
        return 0
    cnt = 1
    for i in range(len(l)-1):
        if l[i+1] - l[i] <= c :
            cnt += 1
        else:
            cnt = 1
    return cnt


n = list(map(strtoInt, input().strip().split(" ")))
c = n[1]
l = list(map(strtoInt, input().strip().split(" ")))
print(func(l,c))