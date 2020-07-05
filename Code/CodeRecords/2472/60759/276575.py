ts = int(input())
for t in range(ts):
    n = int(input())
    lst = list(input())
    for ch in lst:
        if lst.count(ch) == 1:
            print(ch)
            break
    else:
        print('-1')
