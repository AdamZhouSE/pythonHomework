if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    n = int(input())
    # lis = []
    # for item in list:
    #     su = 0
    #     for ite in list:
    #         su += math.ceil(ite/item)
    #     if(su<=n):
    #         lis.append(su)
    # lis = sorted(lis)
    # print(lis[0])
    l, r, ans = 1, max(list) + 1, -1
    while l <= r:
        mid = (l + r) // 2
        total = sum((x - 1) // mid + 1 for x in list)
        if total <= n:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print(ans)
