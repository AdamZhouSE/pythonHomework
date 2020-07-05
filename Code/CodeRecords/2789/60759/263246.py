n = int(input())
for i in range(n):
    num = int(input())
    lst = sorted(list(map(int, input().split(' '))))
    lst.insert(0, 0)
    for idx in range(num):
        if len(lst[idx:]) < lst[idx]:
            print(max(lst[idx - 1], len(lst[idx:])))
            break
    else:
        print(lst.pop())
