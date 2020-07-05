def special_sort(n: int, ls: list) -> list:
    odd = []
    both = []
    for i in ls:
        if i % 2 == 0:
            both.append(i)
        else:
            odd.append(i)
    odd.sort(reverse=True)
    both.sort()
    return odd + both


t = int(input())
res = []
for j in range(t):
    num = int(input())
    lst = input().split(' ')
    lst = list(map(int, lst))
    res.append(special_sort(num, lst))
for j in res:
    for k in range(len(j)):
        print(str(j[k]) + ' ', end='')
    print()