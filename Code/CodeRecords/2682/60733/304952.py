for i in range(int(input())):
    n, l, r = [int(x) for x in input().split()]
    yo = '{:032b}'.format(n)
    lst = list(yo)
    lst.reverse()
    for j in range(l-1,r):
        lst[j] = '1'
    lst.reverse()
    ans = ''.join(lst)
    print(int(ans,2))