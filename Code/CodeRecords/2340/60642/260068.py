def waterVolume():
    input()
    list = [int(i) for i in input().split()]
    volume = 0
    while(len(list)>2):
        fir = max(list)
        firin = list.index(fir)
        list[firin] = 0
        sec = max(list)
        secin = list.index(sec)
        list[firin] = fir
        hight = min(fir,sec)
        idx1 = min(firin,secin)
        idx2 = max(firin,secin)
        for i in range(idx1+1,idx2):
            volume = volume+hight-list[idx1+1]
            list.pop(idx1+1)
        if(list[idx1]>list[idx1+1]):
            list.pop(idx1+1)
        else:
            list.pop(idx1)

    print(volume)


times = int(input())
for i in range(times):
    waterVolume()