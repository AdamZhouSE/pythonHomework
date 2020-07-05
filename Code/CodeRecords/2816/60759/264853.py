n = int(input())
lst = sorted(list(map(int, input().split(' '))))
is1 = True
while len(lst) > 1:
    if is1:
        lst.pop()
    else:
        lst.pop(0)
    is1 = not is1
print(lst[0])
