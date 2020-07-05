def find(lsit, l, r):
    if (r <= l):
        return list[l]
    if(l>r):
        return list[r]
    mid = (l + r) // 2
    if (list[mid] < list[r]):  # 右边按顺序
        minr = list[mid]
        minl = find(list, l, mid - 1)
        return (min(minl, minr))
    else:
        minl = list[l]
        minr = find(list, mid + 1, r)
        return (min(minl, minr))


if __name__ == '__main__':
    temp = input().split(",")
    list = []
    for item in temp:
        list.append(int(item))
    print(find(list,0,len(list)-1))
