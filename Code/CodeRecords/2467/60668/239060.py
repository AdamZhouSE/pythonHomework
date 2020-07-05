def arrays_8_findNum(n,list=[]):
    print(list[n-1])
if __name__ =='__main__':
    de=input()
    list1 = [int(i) for i in input().split()]
    list2 = [int(i) for i in input().split()]
    list3 = [int(i) for i in input().split()]
    li = []
    for item in list3:
        li.append(item)
    for ite in list2:
        li.append(ite)
    li = sorted(li)
    n = list1[2]
    arrays_8_findNum(n,li)