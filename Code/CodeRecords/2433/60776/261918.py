def hebing(list):
    if len(list)==0:
        return [[]]
    else:
        weizi = 0
        list1 = []
        list1.extend(list)
        for i in range(len(list)):
            if list[i][0] < list[weizi][0]:
                weizi = i
        qishi = list[weizi][0]
        zhongzi = list[weizi][1]
        list1.remove(list[weizi])
        list.remove(list[weizi])
        for i in range(0, len(list)):
            if list[i][0] <= zhongzi:
                if list[i][1] > zhongzi:
                    zhongzi = list[i][1]
                list1.remove(list[i])
        list2 = [[qishi, zhongzi]]
        list2.extend(hebing(list1))
        return list2

if __name__ == "__main__":
    a = input().split("],[")
    a[0] = a[0].replace("[[", "")
    a[len(a) - 1] = a[len(a) - 1].replace("]]", "")
    list = []
    for i in range(0, len(a)):
        list.append(a[i].split(','))
    for i in range(0, len(list)):
        for j in range(0, 2):
            list[i][j] = int(list[i][j])
    a=hebing(list)
    if a[len(a)-1]==[]:
        del a[len(a) - 1]
    print(a)
