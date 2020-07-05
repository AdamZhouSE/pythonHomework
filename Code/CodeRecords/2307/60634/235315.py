def update(index,list):
    if index < len(list):
        list[index] += 1
        return list
    else:
        i = len(list)
        while True:
            if i == index:
                list.insert(i,1)
                return list
            else:
                list.insert(i,0)
            i += 1



times = int(input())
while times>0:
    size = int(input())
    str = input()
    #----------
    temp = [0]
    i = 0
    while i < len(str):
        num = ord(str[i])-ord('0')
        temp = update(num,temp)
        i += 2

    #size = (len(str)+1)/4
    max = -1
    i = 0
    while i < len(temp):
        if (temp[i] >= size/2)and(temp[i] > max):
            max = i
        i += 1
        
    print(max)
    #----------
    times -= 1