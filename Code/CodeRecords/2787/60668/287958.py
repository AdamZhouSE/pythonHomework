if __name__=='__main__':
    n = input()
    list = [int(i) for i in input().split()]
    list = sorted(list)
    lis = [int(i) for i in range(1,int(n)+1)]
    co = 0
    for i in range(len(list)):
        co += abs(lis[i]-list[i])
    print(co)