def nums_16_round(list = []):
    co = 0
    for i in range(len(list)):
        con = 0
        for j in range(len(list)):
            con += j*list[j]
        co = max(co,con)
        list = round(list)
    print(co)
def round(list = []):
    list[0],list[1:] = list[-1],list[0:-1]
    return list
if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    nums_16_round(list)