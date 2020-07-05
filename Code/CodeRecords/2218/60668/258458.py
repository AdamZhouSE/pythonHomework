def nums_2_MaxRe(list = []):
    co = 0
    maxN = 0
    list = sorted(list)
    maxN = max(list[0]*list[1]*list[-1],list[-1]*list[-2]*list[-3],list[0]*list[1]*list[2])
    print(maxN)
if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    nums_2_MaxRe(list)