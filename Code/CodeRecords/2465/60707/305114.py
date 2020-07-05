
def Hindex(indexList):
    indexSet = sorted(list(set(indexList)), reverse=True)
    for index in indexSet:
        # clist为大于等于指定引用次数index的文章列表
        clist = [i for i in indexList if i >= index]
        # 由于引用次数index逆序排列，当index<=文章数量len(clist)时，得到H指数
        if index <= len(clist):
            break
    return index


if __name__ == '__main__':
    alist = input().split(",")
    for i in range(len(alist)):
        alist[i] = int(alist[i])
    numIndex = Hindex(alist)
    print(numIndex)