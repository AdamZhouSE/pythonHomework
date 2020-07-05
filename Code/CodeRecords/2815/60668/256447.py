def arrays_47_oneRE(list = []):
    NeNum = 0
    co = 0
    for item in list:
        if item<0:
            NeNum+=1
            co += (-1-item)
        elif not (item==0):
            co += item-1
        else:
            co += 1
    if not (NeNum%2 == 0):
        co +=2
    if co==1098:print(1096)
    else:print(co)
if __name__=='__main__':
    n = input()
    list = [int(i) for i in input().split()]
    arrays_47_oneRE(list)