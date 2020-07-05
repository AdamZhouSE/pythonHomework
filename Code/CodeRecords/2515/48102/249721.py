def search(num: int, ls: list) -> int:
    if num == 1:
        return sum(ls)
    res = []
    for i in range(1, len(ls)-num+1):
        temp = [sum(ls[0:i]), search(num-1, ls[i:])]
        res.append(max(temp))
    return min(res)


lst = input().split(',')
lst = list(map(int, lst))
n = int(input())
print(search(n, lst))