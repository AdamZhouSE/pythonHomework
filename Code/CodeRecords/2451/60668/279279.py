if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    n = int(input())
    if n not in list:
        idx = 0
        for i in range(len(list)):
            if(list[i]<n):
                idx += 1
        print(idx)
    else:
        print(list.index(n))