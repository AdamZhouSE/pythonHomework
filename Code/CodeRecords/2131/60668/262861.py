def nums_19_sameMinus(list = []):
    co = 0
    list = sorted(list)
    for i in range(len(list)-2):
        diff = list[i+1]-list[i]
        for j in range(i+2,len(list)):
            if list[j] - list[j-1]==diff:
                co += 1
            else:
                break
    print(co)
if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    nums_19_sameMinus(list)