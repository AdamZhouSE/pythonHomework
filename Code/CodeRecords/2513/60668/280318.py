if __name__=='__main__':
    list = []
    for _ in range(int(input())):
        re = [int(i) for i in input().split(',')]
        for item in re:
            list.append(item)
    k = int(input())
    list = sorted(list)
    print(list[k-1])