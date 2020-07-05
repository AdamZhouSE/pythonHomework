def arrays_17_Num(low,up,list=[]):
    count = 0
    list_0 = []
    for i in range(0,len(list)):
        co = list[i]
        for j in range(i, len(list)):
            co += list[j]
            list_0.append(co)
    for item in list_0:
        if item>=low and item<=up:
            count += 1
    print(count)
if __name__ == '__main__':
    list = eval(input())
    low = int(input())
    up = int(input())
    arrays_17_Num(low,up,list)