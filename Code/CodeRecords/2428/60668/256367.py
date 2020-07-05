def arrays_44_sortA(list = []):
    list_ord = []
    list_pair = []
    for item in list:
        if item % 2 == 0:
            list_pair.append(item)
        else:
            list_ord.append(item)
    list_ord = sorted(list_ord,reverse=True)
    list_pair =sorted(list_pair)
    list_ord += list_pair
    for i in range(len(list_ord)):
        print(list_ord[i],end = ' ')
    print("")
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        list = [int(i) for i in input().split()]
        arrays_44_sortA(list)