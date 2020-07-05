def search1(width: int, target: int, ls: list) -> int:
    res = []
    for i in ls:
        res += i
    res.sort()
    return res[target-1]


w = int(input())
mat = []
for k in range(w):
    lst = input().split(',')
    lst = list(map(int, lst))
    mat.append(lst)
t = int(input())
print(search1(w, t, mat))