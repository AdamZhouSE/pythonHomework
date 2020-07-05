def arrays_21_sort(list1 = [],list2 = []):
    list = []
    list_0 = []
    for item in list2:
        for i in range(0,len(list1)):
            if list1[i] == item:
                list.append(list1[i])
    for item in list1:
        if item not in list:
            list_0.append(item)
    list_0 = sorted(list_0)
    list += list_0
    print(list)
if __name__ == '__main__':
    list1 = eval(input())
    list2 = eval(input())
    arrays_21_sort(list1,list2)